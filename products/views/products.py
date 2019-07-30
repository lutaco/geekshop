from django.urls import reverse_lazy
from products.models import Product
from products.forms import ProductModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductList(ListView):
	model = Product
	template_name = 'products/index.html'


class ProductUpdate(UpdateView):

	success_url = reverse_lazy('products:list')
	form_class = ProductModelForm
	template_name = 'products/update.html'
	model = Product


class ProductCreate(CreateView):

	form_class = ProductModelForm
	success_url = reverse_lazy('products:list')
	template_name = 'products/create.html'
	model = Product


class ProductDetail(DetailView):

	template_name = 'products/detail.html'
	model = Product


class ProductDelete(DeleteView):

	success_url = reverse_lazy('products:list')
	template_name = 'products/delete.html'
	model = Product
