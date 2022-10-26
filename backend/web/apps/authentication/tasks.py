# -*- coding: utf-8 -*-
#
#
from celery import shared_task
from common.utils import write_login_log
# from celery import shared_task, Task, subtask
import logging

# from celery import shared_task
from config.celery_app import app

logger = logging.getLogger(__name__)

@shared_task
def write_login_log_async(*args, **kwargs):
    write_login_log(*args, **kwargs)
    # pass
