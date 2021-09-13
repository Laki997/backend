from src.users.serializers import UserSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from .permissions import IsUserOrReadOnly


class UserView(GenericViewSet, CreateModelMixin):

    serializer_class = UserSerializer

    permissions = {
        'default': (IsUserOrReadOnly,),
        'create': (AllowAny,)
    }

    def get_permissions(self):
        self.permission_classes = self.permissions.get(
            self.action, self.permissions['default'])
        return super().get_permissions()
