# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import floatformat
from django.utils.translation import ugettext_lazy as _
from authentication.models import User


class Playa(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="person", null=True, blank=True)

    playa_name = models.CharField(_(' playa name'), max_length=20, unique=True, null=False)
    goals = models.IntegerField(_('goals'), default=0)
    own_goals = models.IntegerField(_('own goals'), default=0)
    victorys = models.IntegerField(_('victorys'), default=0)
    defeats = models.IntegerField(_('defeats'), default=0)

    def __unicode__(self):
        return self.playa_name

    class Meta:
        verbose_name = _('playa')
        verbose_name_plural = _('playas')


class Team(models.Model):
    team_name = models.CharField(_('team_name'), max_length=20, unique=True)
    victorys = models.IntegerField(_('victorys'), default=0, editable=False)
    defeats = models.IntegerField(_('defeats'), default=0, editable=False)
    goals = models.IntegerField(_('goals'), default=0, editable=False)
    own_goals = models.IntegerField(_('own goals'), default=0, editable=False)
    users = models.ManyToManyField(User)
    team_icon = models.ImageField(blank=True, null=False, upload_to='pics')
    victory_percentage = models.FloatField(_('win percentage'), default=0)

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')

    def __unicode__(self):
        return self.team_name

    def save(self, *args, **kwargs):
        self.win_percentage = {{float(self.victorys) / self.victorys + self.defeats * 100 | 2}}

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
    excuse = models.CharField(_('excuse'), max_length=200, default='unlucky', null=False)

    class Meta:
        verbose_name = _('match')
        verbose_name_plural = _('matches')

    def save(self, *args, **kwargs):
        if self.goals_team_1 == self.goals_team_2:
            raise ValueError('ties are not allowed')

        if self.goals_team_1 > self.goals_team_2:
            self.winner = self.team_1.team_name
        elif self.goals_team_2 > self.goals_team_1:
            self.winner = self.team_2.team_name

        return super(Match, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{}_{}_{}'.format(self.datum, self.team_1.id, self.team_2.id)
