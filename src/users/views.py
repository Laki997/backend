from rest_framework import status
from src.users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class RegistrationApiView(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'data': serializer.data},
                        status=status.HTTP_201_CREATED)
