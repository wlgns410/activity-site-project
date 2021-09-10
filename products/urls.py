
from django.urls import path
from products.views import ReviewList

urlpatterns = [
    path('review/<int:review_id>', ReviewList.as_view({'get': 'list', "post": "create"})),
]

