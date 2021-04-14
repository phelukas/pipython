from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users import views


urlpatterns = [
    path('create/user/', views.CreateUserView.as_view(), name='user_create'),
    path('update/user/<int:pk>', views.UpdateUserView.as_view(), name='user_update'),
    path('list/users/', views.ListUsersView.as_view(), name='users_list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
