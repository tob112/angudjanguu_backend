# -*- coding: utf-8 -*-placeholder1
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Vector(models.Model):
    name = models.CharField(_('name'), max_length=40)
    wert1 = models.IntegerField(_('wert1'))
    wert2 = models.IntegerField(_('wert2'))
    wert3 = models.IntegerField(_('wert3'))
    wert4 = models.IntegerField(_('wert4'))
    wert5 = models.IntegerField(_('wert5'))

    class Meta:
        verbose_name = _('vector')
        verbose_name_plural = _('vectors')

    def __unicode__(self):
        return self.name


class MessGroese(models.Model):
    name = models.CharField(_('name'), unique=True, max_length=40)

    class Meta:
        verbose_name = _('messgroese')
        verbose_name_plural = _('messgroesen')

    def __unicode__(self):
        return self.name


class Analysis(models.Model):
    name = models.CharField(_('name'), unique=False, max_length=40)
    frequency = models.IntegerField(_('frequency'))
    datasource = models.CharField(_('datasource'), max_length=40)
    placeholder1 = models.CharField(_('placeholder1'), max_length=40)
    placeholder2 = models.CharField(_('placeholder2'), max_length=40)
    placeholder3 = models.CharField(_('placeholder3'), max_length=40)
    vectors = models.ManyToManyField(Vector)
    messgroesen = models.ManyToManyField(MessGroese)

    class Meta:
        verbose_name = _('analysis')
        verbose_name_plural = _('analysis')

    def __unicode__(self):
        return self.name
