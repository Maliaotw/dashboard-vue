# Generated by Django 3.1.7 on 2021-03-02 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiringToken',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authtoken.token',),
        ),
    ]
