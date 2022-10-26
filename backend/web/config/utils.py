# -*- coding: utf-8 -*-
#

import os
import uuid

from django.conf import settings

from config.settings.base import ROOT_DIR


# from common.utils.timezone import local_now

def get_task_log_path(base_path, task_id, level=2):
    task_id = str(task_id)
    try:
        uuid.UUID(task_id)
    except:
        return os.path.join(ROOT_DIR, 'data', 'caution.txt')

    rel_path = os.path.join(*task_id[:level], task_id + '.log')
    path = os.path.join(base_path, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path



def get_celery_task_log_path(task_id):
    return get_task_log_path(settings.CELERY_LOG_DIR, task_id)


