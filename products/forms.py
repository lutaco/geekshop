from django import forms
from .models import Product, Category


class ProductModelForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [
            'name', 'description', 'cost', 'image', 'category'
        ]

        widgets = {
            'name': forms.widgets.TextInput(
                attrs={
                    'class': 'model-form',
                }
            ),
            'description': forms.widgets.Textarea(
                attrs={
                    'class': 'model-form',
                }
            ),
            'cost': forms.widgets.NumberInput(
                attrs={
                    'class': 'model-form',
                }
            ),
            'image': forms.widgets.FileInput(
                attrs={
                    'class': 'model-form',
                }
            ),
            'category': forms.widgets.Select(
                attrs={
                    'class': 'model-form',
                }
            )
        }


class CategoryModelForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = ['name', 'description']

        widgets = {
            'name': forms.widgets.TextInput(
                attrs={
                    'class': 'model-form'
                }
            ),
            'description': forms.widgets.Textarea(
                attrs={
                    'class': 'model-form'
                }
            )
        }
