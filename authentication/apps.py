# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_save
from authentication.models import User
from django.contrib.auth.models import Group


class AuthenticationConfig(AppConfig):
    name = 'authentication'

    def ready(self):
        post_save.connect(User.add_to_default_group, sender=User)
