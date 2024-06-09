from rest_framework import serializers
from django.contrib.auth.models import User
from rental.models import Book, Rental
from django.contrib.auth import get_user_model
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'pages']


class RentalCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
        

class ProlongSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    booktitle = serializers.CharField(max_length=255)
    charges = serializers.FloatField()



class BooksByUserSerializer(serializers.Serializer):
    books_title = serializers.CharField(source='book.title')
    charges = serializers.SerializerMethodField()

    class Meta:
        model = Rental
        fields = ['title', 'charges']

    def get_charges(self, obj):
        rented_at = obj.rented_at.date()
        # print(' rented at ---- > ', rented_at)
        today = datetime.now().date()
        
        delta = today - rented_at
        # print(delta.days)
        if delta.days > 30:
            charges = obj.book.pages / 100
        else:
            charges = 0
        return charges


