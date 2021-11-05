from django.urls import path

from contact.views import contact, contact_list

urlpatterns = [
    path('', contact, name="contact-us"),
    path('list/', contact_list)
    ]
