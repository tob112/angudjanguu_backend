# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    is_admin = models.BooleanField(_('is admin'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    goals = models.IntegerField(_('goals'), default=0)
    own_goals = models.IntegerField(_('own_goals'), default=0)
    victorys = models.IntegerField(_('victorys'), default=0)
    defeats = models.IntegerField(_('defeats'), default=0)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def is_superuser(self):
        return self.is_admin

    # change is_staff to is_admin für die admin seite
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
