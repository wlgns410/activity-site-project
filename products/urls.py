
from django.urls import path
from products.views import ReviewList, CreateReviewList


urlpatterns = [
    path('review/<int:review_id>', ReviewList.as_view({'get': 'list', 'delete' : 'destroy'})),
    path('review', CreateReviewList.as_view())
]

