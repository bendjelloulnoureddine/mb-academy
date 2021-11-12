from django.urls import path
from .views import (
        products,
        product_detail,
        edit_product,
        delete_product,
        category_products
        )

urlpatterns = [
    path('', products, name='product-list'),
    path('detail/<id>', product_detail, name='product-detail'),
    path('edit/<pk>', edit_product, name='product-edit'),
    path('delete/<pk>', delete_product, name='product-delete'),
    path('category/<id>', category_products, name='category-products'),
]


