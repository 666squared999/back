from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from users.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from .serializers import (
    UserSerializer,
)
import jwt
import os


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                **serializer.data,
                "jwts": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                },
            },
            status=status.HTTP_201_CREATED,
        )

class UserMeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user

        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED,
        )