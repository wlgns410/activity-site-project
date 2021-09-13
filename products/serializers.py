from rest_framework.serializers import ModelSerializer

from .models.product import Product
from .models.review import Review
from .models.like import Like


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

class LikeSerializer(ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"