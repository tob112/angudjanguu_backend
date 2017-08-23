# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from kicker.models import Team, Match, Playa


# Register your models here.



class TeamModel(admin.ModelAdmin):
    model = Team
    readonly_fields = ('victorys', 'defeats')
    filter_horizontal = ('playas',)


class MatchModel(admin.ModelAdmin):
    model = Match
    list_display = ['datum', 'team_1', 'team_2', 'goals_team_1', 'goals_team_2', ]
    readonly_fields = ('winner', 'loser')


class PlayaModel(admin.ModelAdmin):
    module = Playa
    readonly_fields = ['goals', 'own_goals', 'victorys', 'defeats', ]


admin.register(Team)(TeamModel)
# admin.register(MessGroesse)(admin.ModelAdmin)
# admin.register(Vector)(admin.ModelAdmin)

admin.register(Match)(MatchModel)
admin.register(Playa)(PlayaModel)
