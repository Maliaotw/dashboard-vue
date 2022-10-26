from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from django_filters import rest_framework as filters

from app import models
from app import serializers


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
        response.data['category'] = serializers.CategorySerializer(models.Category.objects.all(), many=True).data
        response.data['busline'] = serializers.BuslineSerializer(models.Busline.objects.all(), many=True).data

        return response

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AssetListSerializer
        return serializers.AssetSerializer
