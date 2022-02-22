from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.users.views import UserViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
]