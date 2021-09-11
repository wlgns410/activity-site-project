
from django.urls import path
from products.views import ReviewList, ReviewDetail

urlpatterns = [
    path('review', ReviewList.as_view({'get': 'list', "post": "create"})),
    path('modify/<int:pk>', ReviewDetail.as_view()),
]

