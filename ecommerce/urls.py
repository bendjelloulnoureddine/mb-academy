from django.contrib import admin
from django.urls import path, include

from core.views import home

urlpatterns = [
    # Admin Urls
    path('admin/', admin.site.urls),
    # Home Views
    path('', home),
    # Product Urls
    path('product/', include('product.urls')),
    # Contact Urls
    path('contact-us/', include('contact.urls')),
    # Order Urls
    path('order/', include('order.urls')),
]
