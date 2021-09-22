from rest_framework.fields import ReadOnlyField
from src.comments.serializer import CommentSerializer
from rest_framework import serializers
from src.movies.models import Image, Movie, MovieReaction, WatchList


class MovieReactionSeralizer(serializers.ModelSerializer):
    class Meta:
        model = MovieReaction
        fields = ['movie', 'reaction']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image','thumbnail']


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ['movie','watched']


class MovieSerializer(serializers.ModelSerializer):
    isWatched = WatchListSerializer(many=True, read_only=True)
    cover_image = ImageSerializer(read_only=True)
    cover_image_id = serializers.PrimaryKeyRelatedField(source='cover_image', queryset = Image.objects.all(), write_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover_image_id', 'cover_image', 'description', 'genre', 'likes', 'dislikes', 'view_count','isWatched' )
