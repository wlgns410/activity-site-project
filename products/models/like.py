from django.db import models

from products.models.create_time import CreateTime
from products.models.product import Product
from users.models import User

class Like(CreateTime):
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    like    = models.BooleanField(default=False)

    class Meta:
        db_table = 'likes'