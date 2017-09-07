# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from kicker.models import Team, Match, KickerProfile, Game


# Register your models here.



class TeamModel(admin.ModelAdmin):
    model = Team
    readonly_fields = ['goals', 'goals_against', 'victorys', 'defeats', 'victory_percentage']
    filter_horizontal = ('kicker_profiles',)


class MatchModel(admin.ModelAdmin):
    list_display = ['datum', 'team_1', 'team_2', 'goals_team_1', 'goals_team_2', ]
    readonly_fields = ('winner', 'loser')


class KickerProfileModel(admin.ModelAdmin):
    module = KickerProfile
    readonly_fields = ['goals', 'goals_against', 'victorys', 'defeats', ]


class GameModel(admin.ModelAdmin):
    module = Game
    list_display = ['name', 'datum']
    readonly_fields = ['team_one_victorys', 'team_two_victorys', 'game_winner', 'game_loser']
    filter_horizontal = ('matches',)


admin.register(Team)(TeamModel)
# admin.register(MessGroesse)(admin.ModelAdmin)
# admin.register(Vector)(admin.ModelAdmin)

admin.register(Match)(MatchModel)
admin.register(KickerProfile)(KickerProfileModel)
admin.register(Game)(GameModel)
