from rest_framework.fields import ReadOnlyField
from src.comments.serializer import CommentSerializer
from rest_framework import serializers
from src.movies.models import Movie, MovieReaction, WatchList


class MovieReactionSeralizer(serializers.ModelSerializer):
    class Meta:
        model = MovieReaction
        fields = ['movie', 'reaction']


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ['movie','watched']


class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    isWatched = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover_image', 'description', 'genre', 'likes', 'dislikes', 'view_count','comments','isWatched' )
