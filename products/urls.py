
from django.urls import path
from products.views import LikeView, ReviewList, ReviewDetail, ProductList, ProductDetailView

urlpatterns = [
    path('review', ReviewList.as_view({'get': 'list', "post": "create"})),
    path('review/detail/<int:pk>', ReviewDetail.as_view()),
    path('like/<int:pk>', LikeView.as_view()),
    path('product', ProductList.as_view({'get': 'list', "post": "create"})),
    path('product/detail/<int:pk>', ProductDetailView.as_view()),
]

