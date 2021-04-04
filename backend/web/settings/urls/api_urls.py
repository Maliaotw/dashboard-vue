from django.urls import path

from settings import api

app_name = 'settings'

urlpatterns = [

    path('idrac', api.IdracSettingView.as_view()),
    path('vcenter', api.VcenterSettingView.as_view()),
]
