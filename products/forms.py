from django import forms
from . import models


class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ['product_name', 'slug', 'product_description', 'product_thumbnail']

