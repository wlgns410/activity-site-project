from rest_framework.response import Response
from .models.review import Review

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny
from .serializers import ReviewSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView


class ReviewList(ModelViewSet):
                   
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

class CreateReviewList(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(review=request.data)
        return Response({"message":"SUCCESS"}, status = status.HTTP_201_CREATED)

