# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from authentication.models import User


# Register your models here.

# from django.contrib.auth.admin import UserAdmin

class UserModel(admin.ModelAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_active')


admin.register(User)(UserModel)
