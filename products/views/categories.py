from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from products.models import Category
from products.forms import CategoryModelForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from products.serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):

	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoriesList(ListView):
	model = Category
	template_name = 'categories/list.html'


class CategoryDetail(DetailView):

	model = Category
	template_name = 'categories/detail.html'


@login_required(login_url=reverse_lazy('accounts:login'))
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


@login_required(login_url=reverse_lazy('accounts:login'))
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