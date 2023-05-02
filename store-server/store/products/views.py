from django.shortcuts import render, HttpResponse

# Create your views here.

# контроллеры = вьюхи

from .models import *


def main(request):
    return render(request, 'products/Main.html', context)

def index(request):
    return render(request, 'products/index.html')


def order(request):
    return render(request, 'products/Order.html')

def products(request):
    context = {
        'title': 'Store-Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)

def about(request):
    return render(request, 'products/About-Us.html')
