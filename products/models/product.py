from django.db import models

from products.models import CreateTime, Category
from users.models import User

class Product(CreateTime):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    region = models.CharField(max_length=200, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    background_url = models.CharField(max_length=2000, null=True)

    class Meta: 
        db_table = 'products'