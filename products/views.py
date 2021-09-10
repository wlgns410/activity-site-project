from .models.review import Review

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny
from .serializers import ReviewSerializer

class ReviewList(ModelViewSet):
                   
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
