from rest_framework import serializers
from src.movies.serializers import MovieReactionSeralizer, MovieSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Movie, MovieReaction
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from src.movies.models import MovieReaction


class MovieViewSet(ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['^title']
    filterset_fields = ['genre']

    permissions = {
        'default': (IsAuthenticated, ),
    }

    def get_permissions(self):
        self.permission_classes = self.permissions.get(
           self.action, self.permissions['default'])
        return super().get_permissions()

    @action(detail=False, methods=['POST'], url_path='reaction',
            url_name='reaction', authentication_classes=[JWTAuthentication],
            permission_classes=[IsAuthenticated])
    def reaction(self, request):
        serializer = MovieReactionSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        data = serializer.validated_data
        reaction_object = MovieReaction.objects.filter(user=user,
                                                       movie=data['movie']
                                                       ).first()
        data['user'] = user
        if reaction_object is not None and data['reaction'] == reaction_object.reaction:
            data['reaction'] = None
        reaction_object, created = MovieReaction.objects.update_or_create(user=user,
                                                                          movie=data['movie'], defaults=data)
        return Response(MovieReactionSeralizer(reaction_object).data)
