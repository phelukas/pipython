from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.authtoken.views import obtain_auth_token
from users import views
from rest_framework import routers
from .views import *

user_list = UserList.as_view({
    'get': 'list'
})
user_detail = UserList.as_view({
    'get': 'retrieve'
})
user_create = RegisterSerializer.as_view({
    'post': 'create'
})


urlpatterns = format_suffix_patterns([
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('register/', user_create, name='user-create'),
])

# urlpatterns = [
#     path('register/', views.RegisterView.as_view(), name='auth_register'),
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
# ]
