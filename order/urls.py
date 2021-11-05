from django.urls import path

from order.views import add_to_cart

urlpatterns = [
    path('add-to-cart/<id>', add_to_cart, name="add_to_cart"),
    ]
