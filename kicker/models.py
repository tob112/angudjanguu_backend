# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import floatformat
from django.utils.translation import ugettext_lazy as _
from authentication.models import User


class KickerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="person", null=True, blank=True)

    kicker_display_name = models.CharField(_(' playa name'), max_length=20, unique=True, null=False)
    goals = models.IntegerField(_('goals'), default=0)
    own_goals = models.IntegerField(_('own goals'), default=0)
    victorys = models.IntegerField(_('victorys'), default=0)
    defeats = models.IntegerField(_('defeats'), default=0)

    def __unicode__(self):
        return self.kicker_display_name

    class Meta:
        verbose_name = _('kicker_profile')
        verbose_name_plural = _('kicker_Profiles')


class Team(models.Model):
    team_name = models.CharField(_('team_name'), max_length=20, unique=True)
    victorys = models.IntegerField(_('victorys'), default=0, editable=False)
    defeats = models.IntegerField(_('defeats'), default=0, editable=False)
    goals = models.IntegerField(_('goals'), default=0, editable=False)
    own_goals = models.IntegerField(_('own goals'), default=0, editable=False)
    kicker_profiles = models.ManyToManyField(KickerProfile)
    team_icon = models.ImageField(blank=True, null=False, upload_to='pics')
    victory_percentage = models.FloatField(_('win percentage'), default=0, editable=False)

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

    def add_own_goals(self, own_goals):
        self.own_goals += own_goals

    def save(self, *args, **kwargs):
        try:
            self.victory_percentage = (self.victorys * 100) / (self.victorys + self.defeats)
        except Exception as e:
            pass
        return super(Team, self).save(*args, **kwargs)


class Match(models.Model):
    datum = models.DateTimeField(_('datum'), null=False)
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='team_1')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='team_2')
    goals_team_1 = models.IntegerField(_('goals team 1'), null=False, default=0,
                                       validators=[MaxValueValidator(11), MinValueValidator(0)])
    goals_team_2 = models.IntegerField(_('goals team 2'), null=False, default=0,
                                       validators=[MaxValueValidator(11), MinValueValidator(0)])
    winner = models.CharField(_('winner'), max_length=30, editable=False)
    loser = models.CharField(_('loser'), max_length=30, default='change_me', editable=False)
    excuse = models.CharField(_('excuse'), max_length=200, default='unlucky', null=False)

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

    # TODO refactor add_goals und add_own_goals
    def save(self, *args, **kwargs):

        result = self.calc_match_result(self.goals_team_1, self.goals_team_2)

        team_match_winner = result['winner']
        team_match_loser = result['loser']

        self.winner = team_match_winner.team_name
        self.loser = team_match_loser.team_name

        team_match_winner.add_victory()
        team_match_loser.add_defeat()

        self.team_1.add_goals(self.goals_team_1)
        self.team_1.add_own_goals(self.goals_team_2)

        self.team_2.add_goals(self.goals_team_2)
        self.team_2.add_own_goals(self.goals_team_1)

        self.team_1.save()
        self.team_2.save()

        return super(Match, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{}_{}_{}'.format(self.datum, self.team_1.id, self.team_2.id)
