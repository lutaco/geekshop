from django.urls import reverse_lazy, reverse
from products.models import Product
from products.forms import ProductModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.forms.models import model_to_dict


class RestProductList(ListView):

	paginate_by = 4
	model = Product
	template_name = 'products/index.html'

	def get_context_data(self, **kwargs):

		context = super(RestProductList, self).get_context_data(**kwargs)

		data = {}
		page = context.get('page_obj')
		route_url = reverse('rest_products:list')

		data['next_url'] = f'{route_url}?page={page.next_page_number()}' if page.has_next() else None
		data['previous_url'] = f'{route_url}?page={page.previous_page_number()}' if page.has_previous() else None
		data['page'] = page.number
		data['count'] = page.paginator.count

		results = list(map(model_to_dict, page.object_list))
		for i in results:
			i['image'] = i['image'].url if i['image'] else None

		data['results'] = results

		return data

	def render_to_response(self, context, **response_kwargs):
		return JsonResponse(context)



class ProductList(ListView):

	paginate_by = 4
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
