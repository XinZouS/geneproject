# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='blog-home'),
	url(r'^company/$', views.company, name='blog-company'),
	url(r'^about/$', views.about, name='blog-about'),
]

