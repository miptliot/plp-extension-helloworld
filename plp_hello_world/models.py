# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from plp.models import University


class UniversityInstructor(models.Model):
    """
    Пример модели, использующей модели из plp
    """
    name = models.CharField(max_length=500, verbose_name=_(u'Имя преподавателя'))
    university = models.ManyToManyField(University, verbose_name=_(u'Университет'))

    class Meta:
        verbose_name = _(u'Преподаватель университета')
        verbose_name_plural = _(u'Преподаватели университетов')
