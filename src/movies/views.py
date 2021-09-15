from src.movies.serializers import MovieSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Movie
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class MovieViewSet(ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre']

    permissions = {
        'default': (IsAuthenticated, ),
    }

    def get_permissions(self):
        self.permission_classes = self.permissions.get(
           self.action, self.permissions['default'])
        return super().get_permissions()
