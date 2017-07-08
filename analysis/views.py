# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from serializers import AnalysisSerializer, VectorSerializer, MessgroesseSerializer

# Create your views here.
from analysis.models import Analysis, Vector, MessGroesse


class AnalysisViewset(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer


class VectorViewset(viewsets.ModelViewSet):
    queryset = Vector.objects.all()
    serializer_class = VectorSerializer


class MessgroesseViewset(viewsets.ModelViewSet):
    queryset = MessGroesse.objects.all()
    serializer_class = MessgroesseSerializer
