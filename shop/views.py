from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Product
from .models import Category


def product_list(request):
    if request.method == 'GET':
        products_obj = Product.objects.all()

    return render(request, 'shop/list_products.html', {'products': products_obj})


def category_list(request):
    if request.method == 'GET':
        categories_obj = Category.objects.all()

    return render(request, 'shop/list_categories.html', {'categories': categories_obj})