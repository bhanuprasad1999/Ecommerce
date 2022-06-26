from django.db import models
from django.contrib.auth.models import User


class ProductQuantity(models.Model):
    quantity_id = models.AutoField(primary_key=True)
    quantity_uom = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.quantity_uom}'


stock_status = (
    ('outstock', 'Out of Stock'),
    ('instock', 'Stock Avaliable'),
    ('coming', 'Coming soon')
)


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_quantity = models.FloatField()
    product_quantity_uom = models.ForeignKey(
        ProductQuantity, on_delete=models.DO_NOTHING)
    product_seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product_price = models.PositiveIntegerField()
    product_stock_status = models.CharField(
        max_length=100, choices=stock_status, default='instock')


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
