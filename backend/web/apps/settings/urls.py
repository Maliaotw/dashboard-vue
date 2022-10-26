from django.urls import path

from .views import IdracSettingView,VcenterSettingView

app_name = 'settings'

urlpatterns = [

    path('idrac', IdracSettingView.as_view()),
    path('vcenter', VcenterSettingView.as_view()),
]
