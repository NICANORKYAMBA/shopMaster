""" This file contains the views for the store app. """
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ This class defines the product viewset. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer