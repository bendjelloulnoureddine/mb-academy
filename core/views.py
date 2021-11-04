from django.shortcuts import render

from core.models import Slider, SliderImage, WebSite

def home(request):
    slides = SliderImage.objects.filter(slide__id=1)
    return render(
            request,
            'home/index.html',
            context={
                'slide_list': slides
                })
