from src.movies.models import Movie
from rest_framework.response import Response
from src.comments.serializer import CommentSerializer
from src.comments.models import Comments
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie']
    permissions = {
        'default': (IsAuthenticated, ),
    }

    def get_permissions(self):
        self.permission_classes = self.permissions.get(
           self.action, self.permissions['default'])
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        movie = Movie.objects.get(id=data['movie'])
        data['user'] = user
        instance = Comments.objects.create(user=data['user'], movie=movie,
                                           content=data['content'])
        return Response(CommentSerializer(instance).data)
