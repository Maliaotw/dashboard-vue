from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AssetViewSet
from .ws import TaskLogWebsocket

app_name = 'app'

router = DefaultRouter()
router.register(r'asset', AssetViewSet)  # Allow: GET, POST, HEAD, OPTIONS

api_urls = [
    path('', include(router.urls)),
]

ws_urls = [
    path('ws', TaskLogWebsocket.as_asgi(), name='task-log-ws'),
]

urlpatterns = api_urls + ws_urls
