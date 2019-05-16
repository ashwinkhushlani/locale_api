from django.urls import path
from xRides_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('xRides_api/', views.xRidesList.as_view()),
    path('xRides_api/<int:pk>/', views.xRidesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)