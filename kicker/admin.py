# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from kicker.models import Team, Match


# Register your models here.



class TeamModel(admin.ModelAdmin):
    model = Team
    readonly_fields = ('victorys', 'defeats')
    filter_horizontal = ('users',)


class MatchModel(admin.ModelAdmin):
    model = Match
    list_display = ['datum', 'team_1', 'team_2', 'goals_team_1', 'goals_team_2',]


admin.register(Team)(TeamModel)
# admin.register(MessGroesse)(admin.ModelAdmin)
# admin.register(Vector)(admin.ModelAdmin)

admin.register(Match)(MatchModel)
