from rest_framework import serializers

from users.models import UserProfile
from users.serializers import *
from .models import *

class ProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductQuantity
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    # product_quantity_uom = ProductQuantitySerializer(many=False,read_only=True)
    class Meta:
        model = Products
        fields = ['product_id','product_name','product_quantity','product_quantity_uom','product_seller','product_price','product_stock_status']


class OrderSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(many=False)
    class Meta:
        model = Order
        fields = ['order_id', 'order_user', 'product_id', 'quantity']

