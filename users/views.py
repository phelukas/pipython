from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from users.models import User
from users.serializer import RegisterSerializer, UserList

class UserListView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserList
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

class RegisterView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

