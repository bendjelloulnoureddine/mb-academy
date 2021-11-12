from django.urls import path

from order.views import (
        add_to_cart,
        remove_from_cart,
        order_items,
        validate_order
        )

urlpatterns = [
    path('add-to-cart/<id>', add_to_cart, name="add_to_cart"),
    path('delete-from-cart/<id>', remove_from_cart, name="delete_from_cart"),
    path('order/', order_items, name="order-items"),
    path('validate-order/', validate_order, name='validate-order'),
]
