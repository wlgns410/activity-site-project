from django.db import models

from products.models.create_time import CreateTime
from products.models.category import Category
from django.conf import settings

class Product(CreateTime):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    region = models.CharField(max_length=200, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    background_url = models.CharField(max_length=2000, null=True)

    class Meta: 
        db_table = 'products'