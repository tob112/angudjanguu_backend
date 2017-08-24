# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from kicker.models import KickerProfile, Team, Match
from serializers import TeamSerializer, PlayaSerializer, MatchSerializer


# Create your views here.

class PlayaViewset(viewsets.ModelViewSet):
    queryset = KickerProfile.objects.all()
    serializer_class = PlayaSerializer


class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MatchViewset(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
