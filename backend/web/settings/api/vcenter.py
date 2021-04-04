
from rest_framework import status
from rest_framework.views import APIView, Response

from settings import serializers


class VcenterSettingView(APIView):
    """

    """
    serializers_class = serializers.VCENTERSettingSerializer

    def get(self, request, format=None):
        serializer = self.serializers_class()
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
