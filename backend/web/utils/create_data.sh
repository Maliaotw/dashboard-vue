#!/bin/bash

function sync_instance() {
python3 /app/web/manage.py shell << EOF
from app import models
import random

def get_categpry_data():
    return [
        {'name':'虛擬機'},
        {'name':'網路設備'},
        {'name':'服務器'},
    ]


def get_busline_data():
    return [
        {'name':'業務線A'},
        {'name':'業務線B'},
        {'name':'業務線C'}
    ]



for i in range(1000):
    models.Asset.objects.create(
        category=models.Category.objects.get_or_create(**random.choice(get_categpry_data()))[0],
        busline=models.Busline.objects.get_or_create(**random.choice(get_busline_data()))[0]
    )
EOF
}

sync_instance
