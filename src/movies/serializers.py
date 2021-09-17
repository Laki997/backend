from src.comments.serializer import CommentSerializer
from rest_framework import serializers
from src.movies.models import Movie, MovieReaction


class MovieReactionSeralizer(serializers.ModelSerializer):
    class Meta:
        model = MovieReaction
        fields = ['movie', 'reaction']


class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover_image', 'description', 'genre', 'likes', 'dislikes', 'view_count', "comments",)
