from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register('users', views.UserListView)
router.register('register', views.RegisterView)
router_urls = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_urls)),
]
