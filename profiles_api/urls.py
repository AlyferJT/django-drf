from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView

router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")
router.register("profiles", UserProfileViewSet)

urlpatterns = [
    path("hello/", HelloApiView.as_view()),
    path("login/", UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
