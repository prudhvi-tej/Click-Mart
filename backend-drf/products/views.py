from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset=Product.objects.filter(is_active=True)
    serializer_class=ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.filter(is_active=True)
    serializer_class=ProductSerializer





