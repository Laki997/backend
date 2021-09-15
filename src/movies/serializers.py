from rest_framework import serializers
from src.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover_image', 'description', 'genre')
