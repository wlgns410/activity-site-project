
from django.urls import path
from products.views import ReviewList, CreateReviewList

# schedule_detail = ReviewList.as_view({
#     "get": "retrieve",
#     "put": "update",
#     "patch": "partial_update",
#     "delete": "destroy",
# })


urlpatterns = [
    path('review/<int:review_id>', ReviewList.as_view({'get': 'list', 'delete' : 'destroy'})),
    path('review', CreateReviewList.as_view())
]

