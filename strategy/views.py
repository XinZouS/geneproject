# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from strategy.models import Strategy

# pip install django-braces
from braces.views import SelectRelatedMixin


class StrategyCreate(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
	fields = ('name','description')
	model = Strategy


class StrategyDetail(SelectRelatedMixin, generic.DetailView):
	model = Strategy


class StrategyList(SelectRelatedMixin, generic.ListView):
	model = Strategy


class StrategyDelete(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
	model = models.Strategy
	select_related = ('user')
	success_url = reverse_lazy('strategy:all')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user_id=self.request.user.id)

	def delete(self,*args,**kwargs):
		messages.success(self.request,'Strategy Delete Success')
		return super().delete(*args,**kwargs)
