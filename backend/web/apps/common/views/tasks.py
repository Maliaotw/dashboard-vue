from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination

from django_filters import rest_framework as filters

from authentication import models
from app import serializers
from common.tasks import add
import logging
import random

from config.utils import get_celery_task_log_path



logger = logging.getLogger(__name__)



class TaskViewSet(viewsets.GenericViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.AssetSerializer
    pagination_class = LimitOffsetPagination


    @action(detail=False)
    def add(self, request, *args, **kwargs):
        logger.info('add')
        x = random.choice(list(range(10)))
        y = random.choice(list(range(10)))
        task_obj = add.delay(x,y)
        return Response(task_obj.id)

    @action(detail=False)
    def task_detail(self, request, *args, **kwargs):
        logger.info('detail')

        task_id = request.query_params.get('task_id')

        path = get_celery_task_log_path(task_id)
        f = open(path,'r')
        result = f.read()
        return Response(result)