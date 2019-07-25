from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product, Category
from .forms import ProductModelForm, CategoryModelForm


def products_list(request):

	data = Product.objects.all()
	return render(
		request,
		'products/index.html',
		{'object_list': data}
	)


def product_update_view(request, pk):

	obj = get_object_or_404(Product, pk=pk)

	success_url = reverse('products')

	if request.method == 'POST':

		form = ProductModelForm(request.POST, files=request.FILES, instance=obj)
		if form.is_valid():

			form.save()
			return redirect(success_url)

	else:
		form = ProductModelForm(instance=obj)

	return render(request, 'products/update.html', {'form': form})


def product_create_view(request):

	success_url = reverse('products')
	if request.method == 'POST':

		form = ProductModelForm(data=request.POST, files=request.FILES)
		if form.is_valid():

			form.save()
			return redirect(success_url)

	else:
		form = ProductModelForm()

	return render(request, 'products/create.html', {'form': form})


def product_detail_view(request, pk):

	data = get_object_or_404(Product, pk=pk)

	return render(
		request,
		'products/detail.html',
		{'object': data}
	)


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
