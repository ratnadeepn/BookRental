from django.contrib import admin
from django.urls import path, include
from rental.views import UserViewSet, BookViewSet, RentalViewSet


urlpatterns = [
    path('allrentals/', RentalViewSet.as_view({'get': 'list'}), name='all-rentals'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='all-users'),
    path('books/', BookViewSet.as_view({'get': 'list'}), name='all-users'),
    
]