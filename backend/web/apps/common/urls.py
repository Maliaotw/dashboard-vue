from django.conf.urls import include

from .views import HealthzAPIView, DashRackView, DashAssetView, DashBoardView, TaskViewSet
from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = 'common'
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Allow: GET, POST, HEAD, OPTIONS

urlpatterns = [

    path('healthz', HealthzAPIView.as_view(), name='healthz'),
    path('dashboard', DashBoardView.as_view()),
    path('dashasset', DashAssetView.as_view(), name='dashasset'),
    path('dashrack', DashRackView.as_view(), name='dashrack'),
    path('', include(router.urls)),
]
