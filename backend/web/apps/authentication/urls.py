from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LoginListViewSet,ObtainExpiringAuthToken

app_name = 'authentication'

# viewset 配置路由
router = DefaultRouter()
router.register(r'loginlog', LoginListViewSet)  # Allow: GET, POST, HEAD, OPTIONS


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', ObtainExpiringAuthToken.as_view()),
]
