
from common import api
from django.urls import path


app_name = 'common'



urlpatterns = [

    path('healthz', api.HealthzAPIView.as_view(), name='healthz'),
    path('dashboard', api.DashBoardView.as_view()),
    path('dashasset', api.DashAssetView.as_view(), name='dashasset'),
    path('dashrack', api.DashRackView.as_view(), name='dashrack'),

]
