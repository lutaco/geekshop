from django.shortcuts import render

def index(request):
	return render(request, 'mainapp/index.html')

def contacts(request):
	return render(request, 'mainapp/contacts.html')

def about(request):
	return render(request, 'mainapp/about.html')
