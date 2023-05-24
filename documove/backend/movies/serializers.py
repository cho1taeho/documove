from rest_framework import serializers
from .models import Movie, Genre, Giving,Theme


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie

        exclude = ('id', 'like_users')
        read_only_fields = ('genres',)


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieRandomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'genre_ids')

class MovieWishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'genre_ids',)


class GivingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Giving
        fields = '__all__'




class ThemeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Giving, Theme, Movie
        fields = '__all__'