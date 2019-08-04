from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'image', 'cost', 'category'
    ]

    search_fields = [
        'name', 'description', 'category'
    ]

    list_filter = [
        'category'
    ]


class CategoryAdmin(admin.ModelAdmin):

    search_fields = [
        'name', 'description'
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
