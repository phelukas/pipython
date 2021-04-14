from django.urls import path
from core import views

urlpatterns = [
    path("",views.ListPostAPIView.as_view(),name="post_list"),
    path("create/", views.CreatePostAPIView.as_view(),name="post_create"),
    path("update/<int:pk>/",views.UpdatePostAPIView.as_view(),name="update_post"),
    path("delete/<int:pk>/",views.DeletePostAPIView.as_view(),name="delete_post"),
    path("list/posts/<int:pk>/",views.ListOthersPostAPIView.as_view(),name="list_post")
]

