# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Analysis, MessGroese, Vector

# Register your models here.


class AnalysisModel(admin.ModelAdmin):
    model = Analysis
    filter_horizontal = ('vectors','messgroesen')




admin.register(Analysis)(AnalysisModel)
admin.register(MessGroese)(admin.ModelAdmin)
admin.register(Vector)(admin.ModelAdmin)

