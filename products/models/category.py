from django.db  import models
from products.models import CreateTime

class Category(CreateTime): 
    name = models.CharField(max_length=200)

    class Meta: 
        db_table = 'categories'