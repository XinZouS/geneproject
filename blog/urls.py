# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='blog-home'),
	url(r'^company/$', views.company_13rows, name='blog-company'),
	url(r'^advisor/(?P<advisorid>\d+)$', views.advisor_table, name='advisor-table'),
	# url(r'^advisor/<int:advisorid>/$', views.advisor_table, name='advisor-table'),
	# url(r'^advisor/', views.advisor_table, name='advisor-table'),
	url(r'^about/$', views.about, name='blog-about'),
]

