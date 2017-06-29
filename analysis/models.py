# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Analysis(models.Model):
    name = models.CharField(_('name'), unique=False, max_length=40)
    active = models.BooleanField(_('active'), default=False)
    frequency = models.IntegerField(_('frequency'))

    class Meta:
        verbose_name = _('analysis')
        verbose_name_plural = _('analysis')

    def __unicode__(self):
        return self.name
