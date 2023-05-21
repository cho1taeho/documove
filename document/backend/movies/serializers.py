from django.test import TestCase
from .models import Movie, Category
from rest_framework import serializers

# Create your tests here.
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('id', 'like_users')
        read_only_fields = ('genres',)

class MovieRandomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'genre_ids')