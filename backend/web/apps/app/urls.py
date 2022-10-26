from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AssetViewSet

app_name = 'app'


router = DefaultRouter()
router.register(r'asset', AssetViewSet)  # Allow: GET, POST, HEAD, OPTIONS


urlpatterns = [
    path('', include(router.urls)),
]
