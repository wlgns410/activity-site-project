from products.models.product import Product
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models.review import Review
from .models.like import Like

class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"

class LikeSerializer(ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"
