from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from products.models import Category
from products.forms import CategoryModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def category_create_view(request):

	success_url = reverse('products')
	if request.method == 'POST':

		form = CategoryModelForm(data=request.POST)
		if form.is_valid():

			form.save()
			return redirect(success_url)

	else:
		form = CategoryModelForm()

	return render(request, 'categories/create.html', {'form': form})


def category_update_view(request, pk):

	obj = get_object_or_404(Category, pk=pk)

	success_url = reverse('products')

	if request.method == 'POST':

		form = CategoryModelForm(request.POST, instance=obj)
		if form.is_valid():

			form.save()
			return redirect(success_url)

	else:
		form = CategoryModelForm(instance=obj)

	return render(request, 'categories/update.html', {'form': form})