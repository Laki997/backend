from src.movies.serializers import MovieSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Movie
from .permissions import MoviePermissions


class MovieViewSet(GenericViewSet, CreateModelMixin,
                   ListModelMixin):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviePermissions, ]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
