from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
import requests
from rental.models import Book, Rental
from .serializers import RentalCreateSerializer, RentalSerializer, UserRegistrationSerializer, UserSerializer, BooksByUserSerializer, ProlongSerializer
from datetime import datetime

User = get_user_model()



class RentalSetView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = Rental.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RentalCreateSerializer
        return RentalSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("Handling POST request...", request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            user_id = serializer.validated_data['user_id']
            
            user = get_object_or_404(User, id=user_id)

            # Fetch book details from an external API
            response = requests.get(f'https://openlibrary.org/search.json?title={title}')
            # print('external response ....', title, user_id)
            if response.status_code == 200:
                book_data = response.json()
                # print('Book found ....', book_data)
                # Assume the response contains 'title' and 'author' fields
                book_title = book_data['docs'][0]['title']
                book_author = book_data['docs'][0]['author_name'][0]
                book_pages = book_data['docs'][0]['number_of_pages_median']

                # Get or create the book object
                book, created = Book.objects.get_or_create(title=book_title, author=book_author, pages=book_pages)

                # Create the rental object
                rental = Rental.objects.create(user=user, book=book)
                return Response(RentalSerializer(rental).data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Failed to fetch book details'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RentalDeleteView(APIView):
    def get(self, request, rental_id):
        rental = get_object_or_404(Rental, id=rental_id)
        rental.delete()
        return Response({'message': 'Rental has been deleted'}, status=status.HTTP_204_NO_CONTENT)
    

class UserRegistrationView(mixins.ListModelMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    

class ProlongRentalView(APIView):
    def get(self, request, rental_id):
        rental = get_object_or_404(Rental, id=rental_id)
        today = datetime.now().date()
        rented_at_date = rental.rented_at.date()
        delta = today - rented_at_date
        if delta.days > 30:
            charges = rental.book.pages / 100
        else:
            charges = 0

        response_data = {'username': rental.user.username, 'booktitle':rental.book.title ,'charges': charges}
        serializer = ProlongSerializer(response_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BooksByUserView(APIView):
    def get(self, request, user_id):
        rentals = Rental.objects.filter(user_id=user_id)
        serializer = BooksByUserSerializer(rentals, many=True)
        return Response(serializer.data)

            

