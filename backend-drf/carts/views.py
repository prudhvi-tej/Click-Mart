from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart,CartItem
from .serializers import CartSerializer,CartItemSerializer
from rest_framework.response import Response    
from rest_framework import status
from products.models import Product

class CartView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        cart,created=Cart.objects.get_or_create(user=request.user)
        seria=CartSerializer(cart)
        return Response(seria.data,status=status.HTTP_200_OK)

    

class AddtoCart(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        # take the input
        product_id=request.data.get('product_id')
        quantity=request.data.get('quantity')

        if not product_id:
            return Response({'error':'product_id is required'})
        
        # get the product
        product=get_object_or_404(Product,is_active=True,id=product_id)
        # print("Product->",product)

        # Get or Create Cart
        cart,created=Cart.objects.get_or_create(user=request.user)

        # get or create CartItem
        item,created=CartItem.objects.get_or_create(cart=cart,product=product)

        if not created:
            item.quantity+=int(quantity)
            item.save()
        seria=CartSerializer(cart)

        return Response(seria.data,status=status.HTTP_200_OK)
       


class ManageQuantity(APIView):
    permission_classes=[IsAuthenticated]

    def patch(self,request,item_id):
        # Validate
        if 'change' not in request.data:
            return Response({'error':'Provide Change Field'})
        change=int(request.data.get('change'))

        item=get_object_or_404(CartItem,pk=item_id,cart__user=request.user)
        product=item.product

        if change>0:
            if item.quantity+change>product.stock:
                return Response({'error':'Not Enough Stock'})
            
        newqty=item.quantity+change

        if newqty<=0:
            # Remove CartItem from Cart
            item.delete()
            return Response({'Success':'Item Removed'})
        
        item.quantity=newqty
        item.save()
        seria=CartItemSerializer(item)
        return Response(seria.data,status=status.HTTP_200_OK)
    
    def delete(self,request,item_id):
        item=get_object_or_404(CartItem,pk=item_id,cart__user=request.user)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





        





         