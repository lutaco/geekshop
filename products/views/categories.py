from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from products.models import Category
from products.forms import CategoryModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator


class CategoriesList(ListView):
	model = Category
	template_name = 'categories/list.html'


class CategoryDetail(DetailView):

	model = Category
	template_name = 'categories/detail.html'

	def get_context_data(self, **kwargs):

		key = self.context_object_name if self.context_object_name else 'object'

		obj = kwargs.get(key)
		products = obj.product_set.all()
		page_obj = Paginator(products, 4)

		page = self.request.GET.get('page')
		page_obj = page_obj.get_page(page)

		return {key: obj, 'products': page_obj}


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