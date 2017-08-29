from django import forms
from claimapp import models

class nameSearch(forms.Form):
	name = forms.CharField(label = 'name', min_length = 3)
	
	def clean_search(self):
		search = self.cleaned_data.get('person')
		if len(search) < 3 or len(search) > 30:
			raise forms.ValidationError("Please enter a valid name")
		return search
	