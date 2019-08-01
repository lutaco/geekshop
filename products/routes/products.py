from django.urls import path
from products.views import RestProductList


app_name = 'rest_products'

urlpatterns = [
    path('', RestProductList.as_view(), name='list'),
]
