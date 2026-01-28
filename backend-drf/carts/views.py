from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart,CartItem
from .serializers import CartSerializer
from rest_framework.response import Response    
from rest_framework import status

class CartView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        cart,created=Cart.objects.get_or_create(user=request.user)
        seria=CartSerializer(cart)
        return Response(seria.data,status=status.HTTP_200_OK)

        
         