from django.conf.urls import url
from . import views


app_name = 'products'

urlpatterns = [
    url(r'^$', views.products_view, name='list'),
    url(r'^create/$', views.create_view, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.product_view, name='item'),
]
