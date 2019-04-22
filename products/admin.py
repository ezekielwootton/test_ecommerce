from django.contrib import admin
from .models import ProductCategory, ProductBrand, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)

class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_brand', 'product_category', 'product_name', 'product_description',)

# Register your models here.
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(Product, ProductAdmin)

