from django.urls import path
from products.views.categories import (
    category_create_view, category_update_view
)

urlpatterns = [
    path('<int:pk>/update/', category_update_view, name='category_update'),
    path('create/', category_create_view, name='category_create'),
]
