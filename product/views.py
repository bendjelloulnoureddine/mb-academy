from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

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
    # Get the specific product
    product = get_object_or_404(Product, id=pk)

    # Create a product with the data populated
    form = ProductModelForm(
            request.POST or None,
            request.FILES or None, 
            instance=product
    )
    # Check the Type of the request
    if request.method == 'POST':
        form.save()

    context = {
            'form': form
            }
    return render(request,'product/update.html', context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method== 'POST':
        product.delete()
    return HttpResponseRedirect('/')

def poduct_list(request):
    products = Product.objects.all()
    context = {
        'product_list': products
    }
    return render(request, 'product/list.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    
    context = {
        'product': product
    }
    return render(request, 'product/detail.html', context)



# CRUD
