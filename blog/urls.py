# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='blog-home'),
	# url(r'^advisor/(?P<advisorid>\d+)$', views.advisor_table, name='advisor-table'),
	# url(r'^advisor/', views.advisor_table, name='advisor-table'),
	url(r'^fitdefault/', views.fit_default, name='fitdefault'),
	url(r'^about/$', views.about, name='blog-about'),


	# url(r'^autocomplete/$', views.autocomplete, name='autocomplete'),
]

