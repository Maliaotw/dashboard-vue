from rest_framework.views import APIView
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

class HealthzAPIView(APIView):
    # permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        ret = {'code': '0', 'data': [], 'message': f'healthz Hello {request.user}'}
        return Response(ret)
