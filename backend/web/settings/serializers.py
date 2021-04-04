import json

from django.conf import settings
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Setting


class BaseSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            setting = Setting.objects.filter(name=name)
            if setting:
                setting = setting.first()
                if "PASS" in name:
                    value = ""
                else:
                    value = setting.cleaned_value
            else:
                value = getattr(settings, name, None)
            # print(value)
            if value is None:  # and django_value is None:
                continue

            if value is not None:
                if isinstance(value, dict):
                    value = json.dumps(value)
                initial_value = value
            else:
                initial_value = ''
            field.initial = initial_value


    def save(self,category="default" ,**kwargs):

        if not self.is_valid():
            raise ValidationError(self.errors)

        with transaction.atomic():
            # print(self.validated_data.items())

            for name, value in self.validated_data.items():
                field = self.fields[name]
                # print(field)
                if not value:
                    continue
                # if value == getattr(settings, name):
                #     continue

                encrypted = True
                try:
                    setting = Setting.objects.get(name=name)
                except Setting.DoesNotExist:
                    setting = Setting()
                setting.name = name
                setting.category = category
                setting.encrypted = encrypted
                setting.cleaned_value = value
                setting.save()




class IdracSettingSerializer(BaseSerializer):
    IDRAC_USER = serializers.CharField(
        label="IDRAC_USER",

    )
    IDRAC_PASSWD = serializers.CharField(
     label="IDRAC_PASSWD",
    )


class VCENTERSettingSerializer(BaseSerializer):

    VCENTER_SERVER = serializers.CharField(
        label="VCENTER_SERVER",
    )

    VCENTER_USER = serializers.CharField(
     label="VCENTER_USER",
    )

    VCENTER_PASS = serializers.CharField(
     label="VCENTER_PASS",
    )




