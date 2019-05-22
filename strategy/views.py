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
from strategy.forms import StrategyForm


class StrategyCreate(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
	model = Strategy
	form_class = StrategyForm

	login_url = '/login/'
	redirect_field_name = 'blog/advisor_table.html'

	def get_initial(self):
		initial = super(StrategyCreate,self).get_initial()
		return initial
		
	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(StrategyCreate,self).form_valid(form)


class StrategyVerify(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
	model = Strategy
	select_related = ('user',)


class StrategyDetail(SelectRelatedMixin, generic.DetailView):
	model = Strategy
	select_related = ('user',)


# All strategy in a list
class StrategyList(SelectRelatedMixin, generic.ListView):
	model = Strategy
	select_related = ('user',)


# the strategy of current user in a list
class StrategyListByUser(LoginRequiredMixin, generic.ListView):
	model = Strategy
	template_name = 'strategy/strategy_list_by_user.html'

	def get_queryset(self):
		try:
			self.strategy_user = User.objects.prefetch_related('strategies').get(username__iexact=self.kwargs.get('username'))
		except User.DoesNotExist:
			raise Http404
		else:
			return self.strategy_user.strategies.all()

	def get_context_data(self,**kwargs):
		context = super(StrategyListByUser, self).get_context_data(**kwargs)
		context['strategy_user'] = self.strategy_user
		return context


class StrategyDelete(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
	model = Strategy
	select_related = ('user',)
	# success_url = reverse_lazy('strategy:by_user', kwargs={'username': self.object.username})

	def get_queryset(self):
		queryset = super(StrategyDelete, self).get_queryset()
		return queryset.filter(user_id=self.request.user.id)

	def delete(self,*args,**kwargs):
		messages.success(self.request,'Strategy Delete Success')
		return super(StrategyDelete, self).delete(*args,**kwargs)

	def get_success_url(self):
		return reverse_lazy('strategy:by_user', kwargs={'username': self.request.user.username})





