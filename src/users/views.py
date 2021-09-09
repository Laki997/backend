from src.users.serializers import UserSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin


class UserView(GenericViewSet, CreateModelMixin):

    serializer_class = UserSerializer
