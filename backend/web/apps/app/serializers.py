from rest_framework import serializers

from app import models

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Asset
        fields = "__all__"


class AssetListSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source='category.name', required=False)
    busline = serializers.CharField(source='busline.name', required=False)


    class Meta:
        model = models.Asset
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # asset = AssetListSerializer(mary=True)
    class Meta:
        model = models.Category
        fields = "__all__"



class BuslineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Busline
        fields = "__all__"




