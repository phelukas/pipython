from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from users.models import User
from users.serializer import UserCreateSerializer, UserListSerializer

# Classe para controle, precisa configurar na URL para usar
class ListUsersView(ListAPIView):
    "Listar todos os usuarios"

    queryset = User.objects.all()
    serializer_class = UserListSerializer


class CreateUserView(CreateAPIView):
    "Criar um novo usuario"

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer


class UpdateUserView(UpdateAPIView):
    "Editar informações do usuario"

    def get_queryset(self):
        print(self.request.user.pk)
        queryset = User.objects.filter(pk=self.request.user.pk)
        return queryset

    serializer_class = UserCreateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
