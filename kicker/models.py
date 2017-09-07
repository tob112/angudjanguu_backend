# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import floatformat
from django.utils.translation import ugettext_lazy as _
from authentication.models import User


class KickerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="person", null=True, blank=True)

    kicker_display_name = models.CharField(_('display name'), max_length=20, unique=True, null=False)
    goals = models.IntegerField(_('goals'), default=0)
    goals_against = models.IntegerField(_('goals against'), default=0)
    victorys = models.IntegerField(_('victorys'), default=0)
    defeats = models.IntegerField(_('defeats'), default=0)

    def __unicode__(self):
        return self.kicker_display_name

    class Meta:
        verbose_name = _('kicker Profile')
        verbose_name_plural = _('kicker Profiles')


class Team(models.Model):
    team_name = models.CharField(_('team_name'), max_length=20, unique=True)
    victorys = models.IntegerField(_('victorys'), default=0, editable=False)
    defeats = models.IntegerField(_('defeats'), default=0, editable=False)
    goals = models.IntegerField(_('goals'), default=0, editable=False)
    goals_against = models.IntegerField(_('goals_against'), default=0, editable=False)
    kicker_profiles = models.ManyToManyField(KickerProfile)
    team_icon = models.ImageField(blank=True, null=False, upload_to='pics')
    victory_percentage = models.FloatField(_('victory percentage'), default=0, editable=False)

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')

    def __unicode__(self):
        return self.team_name

    def add_victory(self):
        self.victorys += 1

    def add_defeat(self):
        self.defeats += 1

    def add_goals(self, goals):
        self.goals += goals

    def add_goals_against(self, goals_against):
        self.goals_against += goals_against

    def save(self, *args, **kwargs):
        try:
            self.victory_percentage = (self.victorys * 100) / (self.victorys + self.defeats)
        except Exception as e:
            pass
        return super(Team, self).save(*args, **kwargs)


class Match(models.Model):
    datum = models.DateField(_('datum'), null=False)
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='team_1')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='team_2')
    goals_team_1 = models.IntegerField(_('goals team 1'), null=False, default=0,
                                       validators=[MaxValueValidator(9), MinValueValidator(0)])
    goals_team_2 = models.IntegerField(_('goals team 2'), null=False, default=0,
                                       validators=[MaxValueValidator(9), MinValueValidator(0)])

    winner = models.CharField(_('winner'), max_length=30, editable=False)
    loser = models.CharField(_('loser'), max_length=30, editable=False)

    # excuse = models.CharField(_('excuse'), max_length=200, default='unlucky', null=False)

    class Meta:
        verbose_name = _('match')
        verbose_name_plural = _('matches')

    def calc_match_result(self, goals_team_1, goals_team_2):
        if self.goals_team_1 == self.goals_team_2:
            raise ValueError('ties are not allowed')

        result = {}

        if self.goals_team_1 > self.goals_team_2:
            result = {'winner': self.team_1, 'loser': self.team_2}

        elif self.goals_team_2 > self.goals_team_1:
            result = {'winner': self.team_2, 'loser': self.team_1}

        return result

    def save(self, *args, **kwargs):

        result = self.calc_match_result(self.goals_team_1, self.goals_team_2)

        team_match_winner = result['winner']
        team_match_loser = result['loser']

        self.winner = team_match_winner.team_name
        self.loser = team_match_loser.team_name

        team_match_winner.add_victory()
        team_match_loser.add_defeat()

        self.team_1.add_goals(self.goals_team_1)
        self.team_1.add_goals_against(self.goals_team_2)

        self.team_2.add_goals(self.goals_team_2)
        self.team_2.add_goals_against(self.goals_team_1)

        self.team_1.save()
        self.team_2.save()

        return super(Match, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{}: {} vs {} -> {}:{}'.format(self.datum, self.team_1.team_name, self.team_2.team_name,
                                              self.goals_team_1, self.goals_team_2)


class Game(models.Model):
    datum = models.DateField(_('datum'), null=False, auto_now_add=True, blank=True)
    name = models.CharField(max_length=100, default='no name')
    matches = models.ManyToManyField(Match)
    team_one_victorys = models.IntegerField(_('team one victorys'), default=0, null=False)
    team_two_victorys = models.IntegerField(_('team two victorys'), default=0, null=False)
    game_winner = models.CharField(_('game winner'), max_length=30)
    game_loser = models.CharField(_('game loser'), max_length=30)

    def __unicode__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('game')
        verbose_name_plural = _('games')

    def calc_game_score(self, matches):
        counter_team_1 = 0
        counter_team_2 = 0

        result = {}

        for match in matches.all():
            if match.winner == match.team_1.team_name:
                counter_team_1 += 1
            if match.winner == match.team_2.team_name:
                counter_team_2 += 1

        result['team_one'] = counter_team_1
        result['team_two'] = counter_team_2

        return result

    def save(self, *args, **kwargs):

        if not self.id:
            super(Game, self).save(*args, **kwargs)

        result = self.calc_game_score(self.matches)

        self.team_one_victorys = result['team_two']
        # self.team_two_victorys = result

        return super(Game, self).save(*args, **kwargs)
