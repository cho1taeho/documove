from .models import Movie, Theme
from rest_framework import serializers

# Create your tests here.
class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = ('id', 'name',)

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('id', 'videoThumUrl', 'videoUrl',)

class MovieRandomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'theme_ids',)