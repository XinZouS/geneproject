# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.contrib.auth import get_user_model
User = get_user_model()

from blog.models import FitDefault,FitAdvisors,FitCategorys,FitSubAdvisors,FitManagerNames

import misaka


class Strategy(models.Model):
	name = models.CharField(max_length=128)
	slug = models.SlugField(allow_unicode=True)
	user = models.ForeignKey(User,related_name='strategies',on_delete=models.CASCADE)
	description = models.TextField(max_length=256,blank=True,default='')
	description_html = models.TextField(editable=False,default='',blank=True)

	advisors = models.ManyToManyField(FitAdvisors,through='StrategyAdvisor')
	mscats = models.ManyToManyField(FitCategorys,through='StrategyMSCat')
	mssubadvs = models.ManyToManyField(FitSubAdvisors,through='StrategyMSSubAdv')
	mgrnames = models.ManyToManyField(FitManagerNames,through='StrategyMgrName')

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		self.description_html = misaka.html(self.description)
		super(Strategy,self).save(*args,**kwargs)

	def get_absolute_url(self):
		argsdict = {'slug':self.slug, 'pk':self.pk}
		return reverse('strategy:detail',kwargs=argsdict)

	class Meta:
		unique_together = ['user','name']
		ordering = ['name']


class StrategyAdvisor(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='advisors_strategy',on_delete=models.CASCADE)
	Advisor = models.ForeignKey(FitAdvisors,related_name='strategyAdvisorID',on_delete=models.CASCADE)

	def __str__(self):
		return Advisor.Name


class StrategyMSCat(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='mscats_strategy',on_delete=models.CASCADE)
	MSCat = models.ForeignKey(FitCategorys,related_name='strategyMSCat',on_delete=models.CASCADE)

	def __str__(self):
		return MSCat.Name


class StrategyMSSubAdv(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='mssubadvs_strategy',on_delete=models.CASCADE)
	MSSubAdv = models.ForeignKey(FitSubAdvisors,related_name='strategyMSSubAdv',on_delete=models.CASCADE)

	def __str__(self):
		return MSSubAdv.Name


class StrategyMgrName(models.Model):
	strategy = models.ForeignKey(Strategy,related_name='mgrnames_strategy',on_delete=models.CASCADE)
	MgrName = models.ForeignKey(FitManagerNames,related_name='strategyMgrName',on_delete=models.CASCADE)

	def __str__(self):
		return MgrName.Name






