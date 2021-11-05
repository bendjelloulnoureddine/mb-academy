from django.urls import path
from .views import (
        products,
        product_detail,
        edit_product,
        delete_product
        )

urlpatterns = [
    path('products/', products, name='product-list'),
    path('detail/<id>', product_detail, name='product-detail'),
    path('edit/<pk>', edit_product, name='product-edit'),
    path('delete/<pk>', delete_product, name='product-delete')
]


