# Generated by Django 3.1.7 on 2021-03-02 16:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, verbose_name='Username')),
                ('type', models.CharField(choices=[('W', 'Web'), ('T', 'Terminal')], default='W', max_length=2, verbose_name='Login type')),
                ('ip', models.GenericIPAddressField(verbose_name='Login ip')),
                ('city', models.CharField(blank=True, max_length=254, null=True, verbose_name='Login city')),
                ('user_agent', models.CharField(blank=True, max_length=254, null=True, verbose_name='User agent')),
                ('reason', models.SmallIntegerField(choices=[(0, '-'), (1, '用户名/密码 校验失败'), (2, 'MFA authentication failed'), (3, '用户名不存在'), (4, '密碼已過期')], default=0, verbose_name='Reason')),
                ('status', models.BooleanField(choices=[(True, '成功'), (False, '失敗')], default=True, max_length=2, verbose_name='Status')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date login')),
            ],
            options={
                'ordering': ['-datetime', 'username'],
            },
        ),
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='AccessKeyID')),
                ('secret', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='AccessKeySecret')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_keys', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
