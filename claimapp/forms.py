from django import forms
from claimapp import models



class nameSearch(forms.Form):
	name = forms.CharField(label = 'name', min_length = 3)
	
	def clean_search(self):
		search = self.cleaned_data.get('person')
		if len(search) < 3 or len(search) > 30:
			raise forms.ValidationError("Please enter a valid name")
		return search

class dateSearch(forms.Form):
	Dates = forms.DateField(label = 'date')

	def clean_search(self):
		search = self.cleaned_data.get('Dates')
		if len(search) < 8 or len(search) > 11:
			raise forms.ValidationError("invalid date")
		return search


	#def clean_search(self):
	#	if 