from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	template = get_template('mainapp/index.html')
	context = {'name': 'Emperor'}
	return HttpResponse(template.render(context))

def contacts(request):
	rendered_page = render_to_string(
		'mainapp/contacts.html',
		{
			'contacts': [
				'Контакт 1',
				'Контакт 2',
				'Контакт 3',
			]
		}
	)
	return HttpResponse(
		rendered_page
	)

def about(request):
	return render(request, 'mainapp/about.html', {'about_text': 'Это страница!!!'})
