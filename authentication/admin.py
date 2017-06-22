# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from authentication.models import User

# Register your models here.

# from django.contrib.auth.admin import UserAdmin

admin.register(User)(admin.ModelAdmin)