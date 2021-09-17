from rest_framework import serializers
from src.movies.models import Movie, MovieReaction


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover_image', 'description', 'genre', 'likes', 'dislikes')


class MovieReactionSeralizer(serializers.ModelSerializer):
    class Meta:
        model = MovieReaction
        fields = ['movie', 'reaction']
