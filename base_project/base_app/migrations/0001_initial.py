# Generated by Django 4.0.5 on 2022-06-09 07:06

from django.conf import settings
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
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('middle_initial', models.CharField(max_length=150, null=True)),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('image_url', models.CharField(max_length=2000, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'custom_user',
            },
        ),
        # migrations.CreateModel(
        #     name='UserInfo',
        #     fields=[
        #         ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
        #         ('create_datetime', models.DateTimeField(default=django.utils.timezone.now)),
        #         ('create_user', models.CharField(max_length=50)),
        #         ('create_program', models.CharField(max_length=200)),
        #         ('modify_datetime', models.DateTimeField(default=django.utils.timezone.now)),
        #         ('modify_user', models.CharField(max_length=50)),
        #         ('modify_program', models.CharField(max_length=200)),
        #         ('image_url', models.CharField(max_length=2000, null=True)),
        #         ('phone_number', models.CharField(max_length=20, null=True)),
        #         ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
        #     ],
        #     options={
        #         'db_table': 'user_info',
        #         'managed': True,
        #     },
        # ),
    ]
