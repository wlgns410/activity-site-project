from django.db import models

from products.models.create_time import CreateTime
from products.models.product import Product
from django.conf import settings


class Review(CreateTime):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    class Meta:
        db_table = "reviews"