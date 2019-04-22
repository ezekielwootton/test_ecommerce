from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Products(models.Model):
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
