from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category

    class Meta:
        unique_together = ['category']


class ProductBrand(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=64)

    def __str__(self):
        return self.brand

    class Meta:
        unique_together = ['brand']


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, default='none')
    slug = models.CharField(max_length=50, default='none')
    product_description = models.TextField(max_length=5000, default='none')
    product_thumbnail = models.ImageField(default='stars.png', blank=True)
    author = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.product_name

    def snippet(self):
        return self.product_description[:50] + '...'

    def get_absolute_url(self):
        return reverse('products:item', kwargs={'slug': self.slug})
