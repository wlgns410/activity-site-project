from django.core.exceptions import ValidationError
from rest_framework.response import Response
from products.models.product import Product
from .models.review import Review
from .models.like import Like
from .serializers import LikeSerializer, ReviewSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status


class ReviewList(ModelViewSet):
                   
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]


class ReviewDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

	# review의 detail 보기
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

	# review 수정하기
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

	# review 삭제하기
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class LikeView(generics.ListCreateAPIView, mixins.DestroyModelMixin):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        return Like.objects.filter(product=product)

    def perform_create(self, serializer, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer.save(product=Product.objects.get(pk=self.kwargs['pk']))

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("NONE_CONTENT")        