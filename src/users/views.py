from src.users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class RegistrationApiView(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
