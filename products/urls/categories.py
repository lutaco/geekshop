from django.urls import path
from products.views.categories import (
    category_create_view, category_update_view, CategoriesList, CategoryDetail
)


app_name = 'categories'

urlpatterns = [
    path('<int:pk>/update/', category_update_view, name='update'),
    path('create/', category_create_view, name='create'),
    path('', CategoriesList.as_view(), name='list'),
    path('<int:pk>/', CategoryDetail.as_view(), name='detail'),
]
