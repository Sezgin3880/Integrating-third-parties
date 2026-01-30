from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.hotels_by_city, name='hotels_by_city'),
]
