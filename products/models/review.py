from django.db import models

from products.models import CreateTime, Product
from users.models import User


class Review(CreateTime):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    class Meta:
        db_table = "reviews"