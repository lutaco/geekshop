from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:

        model = Product
        fields = ['id', 'name', 'description', 'image', 'cost', 'category']

    def get_category(self, obj):
        if obj.category:
            return obj.category.name
