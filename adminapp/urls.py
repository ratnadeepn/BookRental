from django.contrib import admin
from django.urls import path, include

from adminapp.views import UserRegistrationView, RentalSetView, RentalDeleteView, ProlongRentalView, BooksByUserView


urlpatterns = [
    path('newuser/', UserRegistrationView.as_view(), name='new-user'),
    path('newrental/', RentalSetView.as_view(), name='new-rental'),
    path('deleterental/<int:rental_id>/', RentalDeleteView.as_view(), name='delete-rental'),
    path('prolongrental/<int:rental_id>/', ProlongRentalView.as_view(), name='prolong-rental'),
    path('booksbyuser/<int:user_id>/', BooksByUserView.as_view(), name='books-by-user'),
    
]
