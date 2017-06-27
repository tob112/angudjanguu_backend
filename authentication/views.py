# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_auth.models import TokenModel

from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from authentication.models import User
from authentication.serializers import UserSerializer, LoginSerializer
from rest_framework import permissions
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)


class UserListViewset(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)


sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


# class LoginView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer
#     token_model = TokenModel
#
#     @sensitive_post_parameters_m
#     def dispatch(self, request, *args, **kwargs):
#         return super(LoginView, self).dispatch(*args, **kwargs)
#
#     def process_login(self):
#         django_login(self.request, User)
#
#
#
#     def get_response_serializer(self):
#         if getattr(settings,)