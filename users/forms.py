# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def save(self, *args, **kwargs):
		super(UserRegisterForm, self).save(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

	def save(self, *args, **kwargs):
		super(UserUpdateForm, self).save(*args, **kwargs)


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image',]

	def save(self, *args, **kwargs):
		super(ProfileUpdateForm, self).save(*args, **kwargs)
