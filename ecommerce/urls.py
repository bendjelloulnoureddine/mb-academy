from django.contrib import admin
from django.urls import path, include

from contact.views import contact

urlpatterns = [
    # Admin Urls
    path('admin/', admin.site.urls),
    # Product Urls
    path('', include('product.urls')),
    # Contact Urls
    path('contact-us/', include('contact.urls'))
]
