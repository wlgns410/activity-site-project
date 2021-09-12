
from django.urls import path
from products.views import LikeView, ReviewList, ReviewDetail

urlpatterns = [
    path('review', ReviewList.as_view({'get': 'list', "post": "create"})),
    path('detail/<int:pk>', ReviewDetail.as_view()),
    path('like/<int:pk>', LikeView.as_view())
]

