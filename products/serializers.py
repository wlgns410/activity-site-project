from products.models.product import Product
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models.review import Review

class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


