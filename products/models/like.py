from django.db import models

from products.models.create_time import CreateTime
from products.models.product import Product
from django.conf import settings

class Like(CreateTime):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    like    = models.BooleanField(default=False)

    class Meta:
        db_table = 'likes'