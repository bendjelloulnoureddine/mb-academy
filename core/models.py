from django.db import models

class SliderImage(models.Model):
    image = models.ImageField(upload_to="images/")
    slide = models.ForeignKey('Slider', on_delete=models.SET_NULL, null=True)

class Slider(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class WebSite(models.Model):
    name        = models.CharField(max_length=200)
    url         = models.URLField()
    description = models.TextField(blank=True, null=True)
    address     = models.CharField(max_length=200)
    email       = models.EmailField() 

    def __str__(self):
        return f'{self.name}'

