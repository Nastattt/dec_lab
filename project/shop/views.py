from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ProductAddForm
from .models import Product


def add_product(request):
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            Product.objects.create(name=name, description=description,
                                   price=price)
            return redirect("index")
        else:
            return HttpResponse("Validation failed")
    else:
        form = ProductAddForm()
        return render(request, 'shop/add_product.html', context={'form': form})


def get_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(request, 'shop/index.html',
                      context={'products': products})
