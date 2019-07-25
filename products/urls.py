from django.urls import path
from .views import (
    products_list, product_detail_view, product_create_view, product_update_view,
    category_create_view, category_update_view
)

urlpatterns = [
    path('', products_list, name='products'),
    path('<int:pk>/', product_detail_view, name='detail'),
    path('create/', product_create_view, name='create'),
    path('<int:pk>/update/', product_update_view, name='create'),
    path('category/<int:pk>/update/', category_update_view, name='category_update'),
    path('category/create/', category_create_view, name='category_create'),
]
