from django.contrib import admin
from .models import Product, Category 

class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category__name']
    list_display = ['name', 'buyingPrice', 'sellingPrice', 'quantity']
    class Meta:
        model = Product

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category)

