import logging
import random

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from app import models
from app import serializers
from common.tasks import add

logger = logging.getLogger(__name__)


class AssetsFilter(filters.FilterSet):
    id = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = models.Asset
        fields = ('id', 'category', 'busline')


class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AssetsFilter

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response

    @action(methods=['get'], detail=False)
    def selects(self, request, *args, **kwargs):

        data = {}
        data['category'] = serializers.CategorySerializer(models.Category.objects.all(), many=True).data
        data['busline'] = serializers.BuslineSerializer(models.Busline.objects.all(), many=True).data

        return Response(data)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AssetListSerializer
        return serializers.AssetSerializer

    @action(detail=False)
    def faker(self, request, *args, **kwargs):
        logger.info('faker')
        import random

        def get_categpry_data():
            return [
                {'name': '虛擬機'},
                {'name': '網路設備'},
                {'name': '服務器'},
            ]

        def get_busline_data():
            return [
                {'name': '業務線A'},
                {'name': '業務線B'},
                {'name': '業務線C'}
            ]

        for i in range(1000):
            models.Asset.objects.create(
                category=models.Category.objects.get_or_create(**random.choice(get_categpry_data()))[0],
                busline=models.Busline.objects.get_or_create(**random.choice(get_busline_data()))[0]
            )
        return Response("OK")

    @action(detail=False)
    def faker_bulk(self, request, *args, **kwargs):
        logger.info('faker')
        import random

        def get_categpry_data():
            return [
                {'name': '虛擬機'},
                {'name': '網路設備'},
                {'name': '服務器'},
            ]

        def get_busline_data():
            return [
                {'name': '業務線A'},
                {'name': '業務線B'},
                {'name': '業務線C'}
            ]

        asset_objs = []
        for i in range(1000):
            asset_objs.append(
                models.Asset(
                    category=models.Category.objects.get_or_create(**random.choice(get_categpry_data()))[0],
                    busline=models.Busline.objects.get_or_create(**random.choice(get_busline_data()))[0]
                )
            )

        # models.Asset.objects.bulk_update(asset_objs, ['category', 'busline'])
        models.Asset.objects.bulk_create(asset_objs)

        return Response("OK")

    @action(detail=False)
    def faker_transaction(self):
        from django.db import transaction

        def get_categpry_data():
            return [
                {'name': '虛擬機'},
                {'name': '網路設備'},
                {'name': '服務器'},
            ]

        def get_busline_data():
            return [
                {'name': '業務線A'},
                {'name': '業務線B'},
                {'name': '業務線C'}
            ]

        with transaction.atomic():
            models.Asset.objects.create(
                category=models.Category.objects.get_or_create(**random.choice(get_categpry_data()))[0],
                busline=models.Busline.objects.get_or_create(**random.choice(get_busline_data()))[0]
            )

