# from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from knox.models import AuthToken

from .serializers import ProfileSerializer, RegisterSerializer, LoginSerializer, UserSerializer

# User = settings.AUTH_USER_MODEL


class AccountViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileViewSet(viewsets.ViewSet):
    """
    A ViewSet for update or retrieving profile.
    """
    # def retrieve(self ,request, )
    pass


class settingsViewSet(viewsets.ModelViewSet):
    pass


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            instance, token = AuthToken.objects.create(user=user)
            return Response(
                {
                    'user': UserSerializer(user).data,
                    'token': token,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user_object = serializer.validated_data
            instance, token = AuthToken.objects.create(user=user_object)
            return Response(
                {
                    'user': UserSerializer(user_object).data,
                    'token': token
                }
                ,
                status=status.HTTP_201_CREATED
            )
        return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
