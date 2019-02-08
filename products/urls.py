from django.urls import path
from .views import (
	products_list, product_detail_view
)

urlpatterns = [
    path('', products_list, name='products'),
    path('<int:pk>/', product_detail_view, name='detail')
]
