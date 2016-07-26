# coding: utf-8

from django.conf.urls import url
from plp_hello_world import views


urlpatterns = [
    url(r'^hello-world', views.hello_word, name='hello-world'),
]