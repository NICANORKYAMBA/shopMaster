""" This module defines the product serializer. """
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """ This class defines the product serializer. """
    class Meta:
        model = Product
        fields = '__all__'