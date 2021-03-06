from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, resolve
from django.contrib import messages

from product.models import Product
from order.models import Order, OrderItem

def order_items(request):
    total_price = 0
    try:
        order = Order.objects.filter(is_checked=False)[0]
        for item in order.products.all():
            total_price = total_price + item.product.sellingPrice
    except:
        order = []

    context = {
        'order': order,
        'total_price': total_price

        }
    return render(request, 'order/order_items.html', context)

def validate_order(request):
    order = Order.objects.filter(is_checked=False)[0]
    order.is_checked = True
    order.save()
    return redirect(reverse_lazy('home'))


def add_to_cart(request, id):
    # Get the product
    product = Product.objects.get(id=id)
    # Create Order item
    order_item = OrderItem.objects.create(
            product=product,
            quantity=1,
            promo=0
            )
    try:
        # Get All the Orders
        order = Order.objects.filter(is_checked=False)[0]
    except:
        # Create new Cart
        order = Order.objects.create(
                total_price = 22,
                is_checked=False
                )
    # Add le Product 
    order.products.add(order_item)
    return redirect(reverse_lazy('product-list'))
    #else:
    #   pass
    # Add the new product to the Cart

def remove_from_cart(request, id):
    order_item = get_object_or_404(OrderItem, id=id)
    try:
        # Order.products.filter(product__id=id).exists()
        order = Order.objects.filter(is_checked=False)[0]
        order.products.remove(order_item)
        order_item.delete()
        messages.info(request, 'Produit supprimer avec success')
        return redirect(reverse_lazy('product-list'))

    except:
        messages.error(request, 'Produit / Pannier non trouver.')
        return redirect(reverse_lazy('product-list'))


