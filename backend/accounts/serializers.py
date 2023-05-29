from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Wishlist
from movies.models import Movie
from movies.serializers import MovieWishlistSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    moives = MovieWishlistSerializer(many=True)
    
    class Meta:
        model = Wishlist
        fields = ['user', 'movies', 'created_at',]


class UserbadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'badge',)
