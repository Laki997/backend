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

    @action(detail=False, methods=['POST'], url_name='reaction',
            url_path='reaction',
            permission_classes=[IsAuthenticated],
            authentication_classes=[JWTAuthentication])
    def reaction(self, request, movieId):
         
        user = request.user.id
        reaction_object = MovieReaction.objects.filter(user=user,
                                                       movie=movieId).first()
        new_reaction = request.data['reaction']
        if reaction_object is not None:
            reaction_object.reaction = new_reaction if new_reaction != reaction_object.reaction else None    
        else:
            reaction_object = MovieReaction.objects.create(
                user=request.user.id,
                movie=movieId,
                reaction=new_reaction
            )

        reaction_object.save()
        serializer = MovieReactionSeralizer(reaction_object)
        return Response(serializer.data)
