# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models 


class StrategyAdvisorInline(admin.TabularInline):
	model = models.StrategyAdvisor

class StrategyMSCatInline(admin.TabularInline):
	model = models.StrategyMSCat

class StrategyMSSubAdvInline(admin.TabularInline):
	model = models.StrategyMSSubAdv

class StrategyMgrNameInline(admin.TabularInline):
	model = models.StrategyMgrName


admin.site.register(models.Strategy)

