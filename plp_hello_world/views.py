# coding: utf-8

from django.shortcuts import render
from plp.models import Course


def hello_word(request):
    fields = [(i.attname, i.verbose_name) for i in Course._meta.fields]
    dir_course = dir(Course)
    return render(request, 'hello_word.html', {'fields': fields, 'dir': dir_course})