from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.db.models import Q

from .models import Product
from .forms import (
        CategoryModelForm,
        ProductModelForm
        )

def products(request):
    query = request.GET.get('q')

    if query != '' and query is not None:
        queryset = Product.objects.filter(
                    Q(name__icontains=query)|
                    Q(category__name__icontains=query)
                )
    else:
        queryset = Product.objects.all()

    context = {
         'products': queryset
        }
    return render(request,
            'product/product_list.html',
            context=context)

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
