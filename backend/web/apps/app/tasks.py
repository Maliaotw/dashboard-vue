# -*- coding: utf-8 -*-
#
#
# from celery import shared_task, Task, subtask
import logging

# from celery import shared_task
from config.celery_app import app

logger = logging.getLogger(__name__)


@app.task
def add(x, y):
    logger.info('add')
    logger.info('test')
    logger.info(f'x={x}')
    logger.info(f'y={y}')
    return str(x + y)