from dataclasses import field
from pyexpat import model
from turtle import title
from rest_framework import serializers
from decimal import Decimal
from store.models import Collection, Product

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','featured_product']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price','description','slug','inventory','price_with_taxt','collection']

    price_with_taxt = serializers.SerializerMethodField(method_name='calculate_tax')

    
    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(1.1)
    