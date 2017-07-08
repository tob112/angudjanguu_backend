# -*- coding: utf-8 -*-placeholder1
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Vector(models.Model):
    name = models.CharField(_('name'), max_length=40)
    timeslice_start = models.IntegerField(_('timeslice start'))
    timeslice_end = models.IntegerField(_('timeslice end'))

    class Meta:
        verbose_name = _('vector')
        verbose_name_plural = _('vectors')

    def __unicode__(self):
        return self.name



class MessGroesse(models.Model):
    name = models.CharField(_('name'), unique=True, max_length=40)
    description = models.CharField(_('description'), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _('messgroese')
        verbose_name_plural = _('messgroesen')

    def __unicode__(self):
        return self.name


class Filter(models.Model):
    filter = models.CharField(_('filter'), max_length=500)
    description = models.CharField(_('description'), max_length=50, null=True, blank=True)


class Analysis(models.Model):
    name = models.CharField(_('name'), unique=False, max_length=40)
    datasource = models.CharField(_('datasource'), max_length=40)
    description = models.CharField(_('name'), max_length=100, null=True, blank=True)
    vectors = models.ManyToManyField(Vector)
    messgroesen = models.ManyToManyField(MessGroesse)
    filters = models.ManyToManyField(Filter)

    class Meta:
        verbose_name = _('analysis')
        verbose_name_plural = _('analysis')

    def __unicode__(self):
        return self.name
