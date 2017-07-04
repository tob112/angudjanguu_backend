# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Analysis, MessGroese, Vector

# Register your models here.



admin.register(Analysis)(admin.ModelAdmin)
admin.register(MessGroese)(admin.ModelAdmin)
admin.register(Vector)(admin.ModelAdmin)

