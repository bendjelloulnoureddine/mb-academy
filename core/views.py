from django.shortcuts import render

from core.models import Slider, SliderImage, WebSite
from product.models import Category


def home(request):
    slides = SliderImage.objects.filter(slide__id=1)
    categories = Category.objects.all()

    return render(
            request,
            'home/index.html',
            context={
                'slide_list': slides,
                'category_list': categories
                })
