from django.shortcuts import render

from .models import Product
from .forms import (
        CategoryModelForm,
        ProductModelForm
        )

def home(request):
    product_list  = Product.objects.all()
    form          = CategoryModelForm

    context = {
            'product_list' : product_list,
            'title': 'Mon titre',
            'number': 55,
            'form': form
    }

    return render(request, 'product/index.html', context)

def add_product(request):
    form = ProductModelForm(request.POST or None, request.FILES or None)

    if request.method == POST:
        form.save()
        form = ProductModelForm()
    else: 
        form = ProductModelForm()
    
    context = {
        'form': form
    }
    return render(request, 'product/add_product.html', context)


def edit_product(request, pk):
    pass

def delete_product(request, pk):
    pass

def poduct_list(request):
    pass

def product_detail(request, pk):
    pass
# CRUD
