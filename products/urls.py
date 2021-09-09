from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products.views import ReviewList

urlpatterns = [
    path('review', ReviewList.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)