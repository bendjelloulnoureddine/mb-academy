from django.db import models


class Category(models.Model):
    name            = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name            = models.CharField(max_length=200,blank=True,null=True)
    buyingPrice     = models.FloatField(blank=True,null=True)
    sellingPrice    = models.FloatField(blank=True,null=True)
    quantity        = models.IntegerField(blank=True,null=True)
    description     = models.TextField(blank=True,null=True)
    image           = models.ImageField(blank=True,null=True)
    
    category        = models.ForeignKey('product.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.buyingPrice}'
