from django.shortcuts import render
from django.http import HttpResponse
from claimapp import forms
from claimapp import models
import django_tables2 as tables
# Create your views here.

class pTable(tables.Table):
	class Meta:
		model = models.Speak

class dTable(tables.Table):
	class Meta:
		model = models.Speak

def index (request):

	title = "Main page"
	form = forms.nameSearch(request.POST or None)

	if request.method == 'POST':
		print(request.POST)
		#print(form)

		if form.is_valid():
			print('valid')
			inName = form.cleaned_data['name']

			qs = models.Speak.objects.filter(speaker = inName)
			table = pTable(qs)
			context = {
				'title': title,
				'table': table,
			}
			return render(request, 'view.html', context)
		else:
			print('invalid form!?')
			return HttpResponse('Uhhhh this should\'ve worked') #RENDER TO ANOTHER PAGE AND THE ERRORS/DOUBLE BOX MIGHT STOP!!!!!!!!!!

	elif request.method == 'GET':
		context = {
		'title': title,
		'form': form,
		}

		return render(request, 'home.html',context)

def dates(request):
	title = "Dates"
	form = forms.dateSearch(request.POST or None)

	if request.method == 'POST':

		if form.is_valid():
			inDate = form.cleaned_data['Dates']

			qs = models.Speak.objects.filter(date = inDate)
			table = dTable(qs)

			context = {
				'tilte': title,
				'table': table,
			}
			return render(rquest, 'Dates.html', context)
		else:
			print(form.errors)
			return HttpResponse('REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\t' + str(form.errors)) #RENDER TO ANOTHER PAGE AND THE ERRORS MIGHT STOP!!!!!!!!!!
	#elif request.method == 'GET':
	else:
		context = {
		'title': title,
		'form': form,
		}
		return render(request, 'Dates.html', context)