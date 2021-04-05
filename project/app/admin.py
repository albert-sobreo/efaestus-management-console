from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'is_authenticated')

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'deadline', 'status')

class BugAdmin(admin.ModelAdmin):
    list_display = ('issue_no', 'title', 'date_created', 'status', )




admin.site.register(User, UserAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Bug, BugAdmin)