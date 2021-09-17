from rest_framework import serializers
from src.comments.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['content', 'movie']
