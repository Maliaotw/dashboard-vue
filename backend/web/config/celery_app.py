import logging
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.signals import after_setup_logger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("web")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.timezone = 'Asia/Taipei'
app.conf.task_soft_time_limit = 300
app.conf.task_time_limit = 600
app.conf.worker_max_tasks_per_child = 40
app.conf.broker_heartbeat = 0
app.conf.task_acks_late = True

app.conf.broker_transport_options = {'visibility_timeout': 43200}

app.conf.task_default_queue = 'celery'


# -*- coding: utf-8 -*-
#


# from .utils import get_logger
import logging
# from .decorator import get_after_app_ready_tasks, get_after_app_shutdown_clean_tasks
from .logger import CeleryThreadTaskFileHandler

logger = logging.getLogger(__file__)
safe_str = lambda x: x


# @worker_ready.connect
# def on_app_ready(sender=None, headers=None, **kwargs):
#     if cache.get("CELERY_APP_READY", 0) == 1:
#         return
#     cache.set("CELERY_APP_READY", 1, 10)
#     tasks = get_after_app_ready_tasks()
#     logger.debug("Work ready signal recv")
#     logger.debug("Start need start task: [{}]".format(", ".join(tasks)))
#     for task in tasks:
#         subtask(task).delay()


# @worker_shutdown.connect
# def after_app_shutdown_periodic_tasks(sender=None, **kwargs):
#     if cache.get("CELERY_APP_SHUTDOWN", 0) == 1:
#         return
#     cache.set("CELERY_APP_SHUTDOWN", 1, 10)
#     tasks = get_after_app_shutdown_clean_tasks()
#     logger.debug("Worker shutdown signal recv")
#     logger.debug("Clean period tasks: [{}]".format(', '.join(tasks)))
#     PeriodicTask.objects.filter(name__in=tasks).delete()


@after_setup_logger.connect
def add_celery_logger_handler(sender=None, logger=None, loglevel=None, format=None, **kwargs):
    if not logger:
        return
    task_handler = CeleryThreadTaskFileHandler()
    task_handler.setLevel(loglevel)
    formatter = logging.Formatter(format)
    task_handler.setFormatter(formatter)
    logger.addHandler(task_handler)

