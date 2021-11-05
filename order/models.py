from django.db import models

import uuid


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    products    = models.ManyToManyField('order.OrderItem', blank=True)
    is_checked  = models.BooleanField()
    date       = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}'

class OrderItem(models.Model):
    product     = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    promo       = models.FloatField()
    date        = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.product.name}'
