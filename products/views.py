from .models.review import Review
from .serializers import ReviewSerializer
from rest_framework import generics
from rest_framework import mixins


class ReviewList(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
                   
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # 생성하기
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # 조회하기
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # 수정하기
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # 삭제하기
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
