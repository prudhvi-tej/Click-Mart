from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=6)
    stock=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


    
