# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# pip install django-braces
from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()

from strategy.models import Strategy


class StrategyCreate(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
	fields = ('name','description')
	model = Strategy


class StrategyDetail(SelectRelatedMixin, generic.DetailView):
	model = Strategy


# All strategy in a list
class StrategyList(SelectRelatedMixin, generic.ListView):
	model = Strategy
	select_related = ('user','strategy')


# the strategy of current user in a list
class StrategyListByUser(LoginRequiredMixin, generic.ListView):
	model = Strategy
	template_name = 'strategy/list_by_user.html'

	def get_queryset(self):
		try:
			self.strategy_user = User.objects.prefetch_related('strategies').get(username__iexact=self.kwargs.get('username'))
		except User.DoesNotExist:
			raise Http404
		else:
			return self.strategy_user.strategies.all()

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['strategy_user'] = self.strategy_user
		return context


class StrategyDelete(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
	model = Strategy
	select_related = ('user')
	success_url = reverse_lazy('strategy:all')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user_id=self.request.user.id)

	def delete(self,*args,**kwargs):
		messages.success(self.request,'Strategy Delete Success')
		return super().delete(*args,**kwargs)
