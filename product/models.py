from django.db import models


class Category(models.Model):
    name            = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name            = models.CharField(max_length=200)
    buyingPrice     = models.FloatField(blank=True,null=True)
    sellingPrice    = models.FloatField()
    quantity        = models.IntegerField()
    description     = models.TextField()
    image           = models.ImageField()
    
    category        = models.ForeignKey('product.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.buyingPrice}'
