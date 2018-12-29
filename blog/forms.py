from django import forms


class AdvisorForm(forms.Form):
	advId = forms.IntegerField()
	advName = forms.CharField()


