from django import forms
from blog.models import FitDefault,FitAdvisors,FitCategorys,FitSubAdvisors,FitManagerNames
from strategy.models import Strategy

class StrategyForm(forms.ModelForm):
	advisors = forms.ModelMultipleChoiceField(
		queryset=FitAdvisors.objects.none(),
		widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)
	mscats = forms.ModelMultipleChoiceField(
		queryset=FitCategorys.objects.none(),
		widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)
	mssubadvs = forms.ModelMultipleChoiceField(
		queryset=FitSubAdvisors.objects.none(),
		widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)
	mgrnames = forms.ModelMultipleChoiceField(
		queryset=FitManagerNames.objects.none(),
		widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)

	class Meta():
		model = Strategy
		fields = ('name','description','advisors','mscats','mssubadvs','mgrnames')

		widgets = {
			'name':forms.TextInput(attrs={'class':'textinputclass'}), # for CSS:
			'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
		}

	def __init__(self, *args, **kwargs):
		print("---- init form kwargs ------------------------")
		print(kwargs)

		super(StrategyForm, self).__init__(*args,**kwargs)
		if kwargs.get('initial'):
			initDict = kwargs['initial']
			# self.fields['name'].initial = initDict['name']
			advIds = initDict['advId']
			catIds = initDict['catId']
			subIds = initDict['subId']
			mgrIds = initDict['mgrId']

			if advIds:
				print('----    get advId for initial: ', advIds, FitAdvisors.objects.filter(pk__in=advIds))
				self.fields["advisors"].initial = (
					FitAdvisors.objects.filter(pk__in=initDict['advId'])
				)
			if catIds:
				print('----    get catId for initial')
				self.fields["mscats"].initial = (
					FitCategorys.objects.filter(pk__in=catIds)
				)
			if subIds:
				print('----    get subId for initial')
				self.fields["mssubadvs"].initial = (
					FitSubAdvisors.objects.filter(pk__in=subIds)
				)
			if mgrIds:
				print('----    get mgrId for initial')
				self.fields["mgrnames"].initial = (
					FitManagerNames.objects.filter(pk__in=mgrIds)
				)








