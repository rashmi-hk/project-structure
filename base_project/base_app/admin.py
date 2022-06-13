from django.contrib import admin

# Register your models here.
from .models import EmployeeInfo


class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'title')
