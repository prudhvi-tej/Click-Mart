from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart,CartItem
from rest_framework.response import Response
from .models import Order,OrderItem
from rest_framework.serializers import Serializer
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework import status
from .utils import send_order_notification
from rest_framework.generics import ListAPIView


class PlaceOrderView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        cart=Cart.objects.get(user=request.user)
        shipping_address=request.data.get("shippingAddress")
        # Check if Cart is Empty
        if not cart or cart.items.count()==0:
            return Response({'error':'Cart is Empty'})
        
        # Create the Order
        order=Order.objects.create(
            user=request.user,
            subtotal=cart.subtotal,
            tax_amount=cart.tax_amount,
            grand_total=cart.grand_total,
            address=shipping_address.get("address"),
            phone=shipping_address.get("phone"),
            city=shipping_address.get("city"),
            state=shipping_address.get("state"),
            zip_code=shipping_address.get("zip_code"),
        )

        # Create Order Items
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
                total_price=item.total_price,
            )
        
        # Clear CartItems
        cart.items.all().delete()
        cart.save()

        # Send Email Notification
        send_order_notification(order)

        # Send Response
        seria=OrderSerializer(order)
        return Response(seria.data,status=status.HTTP_201_CREATED)
    

class MyOrderView(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    



