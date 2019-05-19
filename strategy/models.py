# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.contrib.auth import get_user_model
User = get_user_model()

from blog.models import Advisors,MSCats,MSSubAdvs,MgrNames

import misaka


class StrategyAdvisor(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='advisors',on_delete='CASCADE')
	Advisor = models.ForeignKey(Advisors,related_name='strategyAdvisorID',on_delete='CASCADE')

	def __str__(self):
		return Advisor.Name

class StrategyMSCat(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='mscats',on_delete='CASCADE')
	MSCat = models.ForeignKey(MSCats,related_name='strategyMSCat',on_delete='CASCADE')

	def __str__(self):
		return MSCat.Name

class StrategyMSSubAdv(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='mssubadvs',on_delete='CASCADE')
	MSSubAdv = models.ForeignKey(MSSubAdvs,related_name='strategyMSSubAdv',on_delete='CASCADE')

	def __str__(self):
		return MSSubAdv.Name

class StrategyMgrName(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='mgrnames',on_delete='CASCADE')
	MgrName = models.ForeignKey(MgrNames,related_name='strategyMgrName',on_delete='CASCADE')

	def __str__(self):
		return MgrName.Name


class Strategy(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(allow_unicode=True)
	user = models.ForeignKey(User,related_name='strategies',on_delete='CASCADE')
	description = models.TextField(max_length=255,blank=True,default='')
	description_html = models.TextField(editable=False,default='',blank=True)

	advisors = models.ManyToManyField(Advisors,through='StrategyAdvisor')
	mscats = models.ManyToManyField(MSCats,through='StrategyMSCat')
	mssubadvs = models.ManyToManyField(MSSubAdvs,through='StrategyMSSubAdv')
	mgrnames = models.ManyToManyField(MgrNames,through='StrategyMgrName')

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		self.description_html = misaka.html(self.description)
		super().save(*args,**kwargs)

	def get_absolute_url(self):
		argsdict = {'slug':self.slug, 'pk':self.pk}
		return reverse('strategy:details',kwargs=argsdict)

	class Meta:
		ordering = ['name']


