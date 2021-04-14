from django.urls import path
from core import views

urlpatterns = [
    path("", views.ListPostAPIView.as_view(), name="post_list"),
    path("create/post/", views.CreatePostAPIView.as_view(), name="post_create"),
    path("update/post/<int:pk>/",
         views.UpdatePostAPIView.as_view(), name="update_post"),
    path("delete/post/<int:pk>/",
         views.DeletePostAPIView.as_view(), name="delete_post"),
    path("list/posts/<int:pk>/",
         views.ListOthersPostAPIView.as_view(), name="list_post")
]
