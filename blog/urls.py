# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
	url(r'^$', views.home, name='blog-home'),
	url(r'^fitdefault/', views.fit_default, name='fitdefault'),
	url(r'^about/$', views.about, name='about'),


	# url(r'^autocomplete/$', views.autocomplete, name='autocomplete'),
]

