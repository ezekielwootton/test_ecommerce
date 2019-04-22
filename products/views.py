from django.shortcuts import render, redirect
from .models import Products
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def products_view(request):
    products = Products.objects.all()
    return render(request, 'products/products_list_view.html', {'products': products})

def product_view(request, slug):
    product = Products.objects.get(slug=slug)
    return render(request, 'products/product_view.html', {'product': product})

@login_required(login_url='/accounts/login/')
def create_view(request):
    if request.method == 'POST':
        form = forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('products:list')
    else:
        form = forms.CreateProduct()
    return render(request, 'products/create.html', {'form': form})
