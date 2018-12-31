from django import forms


class AdvisorForm(forms.Form):
	advId = forms.IntegerField(widget=forms.HiddenInput(), required = False)
	advName = forms.CharField(widget=forms.HiddenInput(), required = False)

class AdvisorsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        advs = kwargs.pop('advisors')
        super(AdvisorsForm, self).__init__(*args, **kwargs)
        counter = 1
        for a in advs:
            self.fields['advId-' + str(counter)] = forms.CharField(widget=forms.HiddenInput())
            counter += 1

