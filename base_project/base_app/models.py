
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
# from jsonfield import JSONField
#
# from .manager import CustomUserManager


class Tracker(models.Model):
    # Set PK for all models
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # tracker columns
    create_datetime = models.DateTimeField(default=now, null=False, blank=False)
    create_user = models.CharField(max_length=50)
    create_program = models.CharField(max_length=200)
    modify_datetime = models.DateTimeField(default=now, null=False, blank=False)
    modify_user = models.CharField(max_length=50)
    modify_program = models.CharField(max_length=200)

    class Meta:
        abstract = True


class UserInfo(Tracker):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2000, null=True)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "%s | %s" % (self.user_id, self.image_url)

    class Meta:
        managed = True
        db_table = 'user_info'


class EmployeeInfo(Tracker):
    name = models.CharField(max_length=2000, null=False)
    department = models.CharField(max_length=2000, null=False)
    address = models.CharField(max_length=2000, null=False)
    roll = models.BigIntegerField(null=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return "%s | %s" % (self.name, self.roll)

    class Meta:
        managed = True
        db_table = 'Employee_info'

