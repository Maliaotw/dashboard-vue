import json
import os
import threading
import time

from channels.generic.websocket import JsonWebsocketConsumer
from django.db.utils import (
    ConnectionHandler,
)

from common.utils import get_logger
from config.utils import get_celery_task_log_path

logger = get_logger(__name__)

connections = ConnectionHandler()

# 复制 django.db.close_old_connections, 因为它没有导出，ide 提示有问题
def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()



class TaskLogWebsocket(JsonWebsocketConsumer):
    disconnected = False

    log_types = {
        'celery': get_celery_task_log_path,
    }

    def connect(self):
        user = self.scope["user"]
        self.accept()
        # if user.is_authenticated:
        #     self.accept()
        # else:
        #     self.close()

    def get_log_path(self, task_id):
        func = self.log_types.get(self.log_type)
        if func:
            return func(task_id)

    def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = json.loads(text_data)
        task_id = data.get('task')
        self.log_type = data.get('type', 'celery')
        if task_id:
            self.handle_task(task_id)

    def wait_util_log_path_exist(self, task_id):
        log_path = self.get_log_path(task_id)
        while not self.disconnected:
            if not os.path.exists(log_path):
                self.send_json({'message': '.', 'task': task_id})
                time.sleep(0.5)
                continue
            self.send_json({'message': '\r\n'})
            try:
                logger.debug('Task log path: {}'.format(log_path))
                task_log_f = open(log_path, 'rb')
                return task_log_f
            except OSError:
                return None

    def read_log_file(self, task_id):
        task_log_f = self.wait_util_log_path_exist(task_id)
        if not task_log_f:
            logger.debug('Task log file is None: {}'.format(task_id))
            return

        task_end_mark = []
        while not self.disconnected:
            data = task_log_f.read(4096)
            if data:
                data = data.replace(b'\n', b'\r\n')
                self.send_json(
                    {'message': data.decode(errors='ignore'), 'task': task_id}
                )
                if data.find(b'succeeded in') != -1:
                    task_end_mark.append(1)
                if data.find(bytes(task_id, 'utf8')) != -1:
                    task_end_mark.append(1)
            elif len(task_end_mark) == 2:
                logger.debug('Task log end: {}'.format(task_id))
                break
            time.sleep(0.2)
        task_log_f.close()

    def handle_task(self, task_id):
        logger.info("Task id: {}".format(task_id))
        thread = threading.Thread(target=self.read_log_file, args=(task_id,))
        thread.start()

    def disconnect(self, close_code):
        self.disconnected = True
        self.close()
        close_old_connections()
