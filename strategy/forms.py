from django import forms
from blog.models import Advisors,MSCats,MSSubAdvs,MgrNames
from strategy.models import Strategy

class StrategyForm(forms.ModelForm):
	advisors = forms.ModelMultipleChoiceField(
		queryset=Advisors.objects.none(),
		# widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)
	mscats = forms.ModelMultipleChoiceField(
		queryset=MSCats.objects.none(),
		# widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)
	mssubadvs = forms.ModelMultipleChoiceField(
		queryset=MSSubAdvs.objects.none(),
		# widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)
	mgrnames = forms.ModelMultipleChoiceField(
		queryset=MgrNames.objects.none(),
		# widget = forms.CheckboxSelectMultiple(attrs={'checked':''})
		)

	def __init__(self, *args, **kwargs):
		qsAdvisors = kwargs.pop('selectedAdvisorIds')
		super(StrategyForm, self).__init__(*args,**kwargs)
		self.fields['advisors'].queryset = qsAdvisors

	class Meta():
		model = Strategy
		fields = ('name','description','advisors','mscats','mssubadvs','mgrnames')

		widgets = {
			'name':forms.TextInput(attrs={'class':'textinputclass'}), # for CSS:
			# 'name':forms.CharField(attrs={'class':'textinputclass'}), # for CSS:
			'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
		}
