from rest_framework import serializers
from .models import Cart,CartItem



class CartItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source='product.name',read_only=True)
    price=serializers.DecimalField(source='product.price',max_digits=10,decimal_places=2,read_only=True)
    tax_percent=serializers.DecimalField(source='product.tax_percent',max_digits=10,decimal_places=2,read_only=True)
    class Meta:
        model=CartItem
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    subtotal=serializers.DecimalField(max_digits=10,decimal_places=2)
    tax_amount=serializers.DecimalField(max_digits=10,decimal_places=2)
    grand_total=serializers.DecimalField(max_digits=10,decimal_places=2)
    items=CartItemSerializer(many=True)
    class Meta:
        model=Cart
        fields="__all__"

    @property
    def get_total(self,obj):
        total=0
        for item in obj.items.all():
            sub=item.product.price*item.quantity
            tax=sub*(item.product.tax_percent/100)
            total+=sub+tax
        return total
