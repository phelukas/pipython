from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from core.serializer import PostSerializer, PostCreateSerializer, PostListSerializer
from core.models import Post as Posts


class ListPostAPIView(ListAPIView):
    "Listar todos os posts de todos os usuarios"

    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class CreatePostAPIView(CreateAPIView):
    "Criar posts"

    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UpdatePostAPIView(UpdateAPIView):
    "Editar posts"

    def get_queryset(self):
        queryset = Posts.objects.filter(criado_por=self.request.user)
        return queryset

    serializer_class = PostCreateSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DeletePostAPIView(DestroyAPIView):
    "Deletar posts"

    def get_queryset(self):
        queryset = Posts.objects.filter(criado_por=self.request.user)
        return queryset

    serializer_class = PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListOthersPostAPIView(ListAPIView):
    "Listar os posts dos outros usuarios"

    def get_queryset(self):
        queryset = Posts.objects.exclude(criado_por=self.request.user)
        return queryset

    serializer_class = PostListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
