# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # für die rest api -> user zugriff /users/username anstatt /users/pk
    lookup_field = 'username'
    serializer_class = UserSerializer
    queryset = User.objects.all()
