from src.settings import CONFIGURABLE_EMAIL

from src.movies.serializers import MovieReactionSeralizer, MovieSerializer, WatchListSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Movie, MovieReaction, WatchList
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from src.movies.models import MovieReaction
from django.db.models import Count, Q
from django.core.mail import send_mail


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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

        movie = Movie.objects.get(id=data['movie'].id)
        return Response(MovieSerializer(movie).data)

    @action(detail=False, methods=['POST'], url_name="watchlist", url_path='watchlist',
            authentication_classes=[JWTAuthentication],
            permission_classes=[IsAuthenticated])
    def watchlist(self, request):
        serializer = WatchListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        data = serializer.validated_data
        watchlist_object = WatchList.objects.filter(user=user, movie=data['movie']).first()
        data['user'] = user

        watchlist_object, created = WatchList.objects.update_or_create(user=user, movie=data['movie'], defaults=data)
        movie = Movie.objects.get(id=data['movie'].id)
        return Response(MovieSerializer(movie).data)

    @action(detail=False, methods=['GET'], url_name='popular',
            url_path='popular',
            authentication_classes=[JWTAuthentication], permission_classes=[IsAuthenticated])
    def popular(self, request):
        popular_movies = Movie.objects.annotate(movie_likes=Count('reactions',
                                                filter=Q(reactions__reaction=True))).order_by('-movie_likes')[:10]
        serializer = MovieSerializer(popular_movies, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'], url_path=r'related/(?P<pk>\w+)',
            url_name='related',
            permission_classes=[IsAuthenticated],
            authentication_classes=[JWTAuthentication])
    def related(self, request, pk):
        movie = Movie.objects.get(id=pk)     
        related_movies = Movie.objects.filter(genre=movie.genre).exclude(id=pk).order_by('title')[:10]
        serializer = MovieSerializer(related_movies, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(CONFIGURABLE_EMAIL)
        title = request.data['title']
        description = request.data['description']
        genre = request.data['genre'] 
        message = 'New movie is added: Title: ' + ' ' + title + ' ' + 'Description: ' + ' ' + description +  ' ' +  'Genre: ' + genre
        send_mail('New Movie', message , 'lazarkalajdzic@gmail.com',
                 [CONFIGURABLE_EMAIL])
        return super().create(request, *args, **kwargs)
