# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from authentication.models import User


# Create your models here.

#
class Team(models.Model):
    team_name = models.CharField(_('team_name'), max_length=20)
    victorys = models.IntegerField(_('victorys'), default=0, editable=False)
    defeats = models.IntegerField(_('defeats'), default=0, editable=False)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.team_name


class Match(models.Model):
    datum = models.DateTimeField(_('datum'), null=False)

    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='team_1')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='team_2')

    goals_team_1 = models.IntegerField(_('goals_team_1'), null=False, default=0)
    goals_team_2 = models.IntegerField(_('goals_team_2'), null=False, default=0)
    result = models.CharField(_('result'), max_length=30, editable=False)

    def save(self, *args, **kwargs):

        if self.goals_team_1 == self.goals_team_2:
            raise ValueError('ties are not allowed')

        if self.goals_team_1 > self.goals_team_2:
            self.result = self.team_1.team_name
        elif self.goals_team_2 < self.goals_team_1:
            self.result = self.team_2.team_name

        return super(Match, self).save(*args, **kwargs)
