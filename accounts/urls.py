from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="users")


urlpatterns = [
    path("", views.UserDetail.as_view(), name="user-detail"),
    path("", include(router.urls)),
]
