from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CreateUserView,
    UserMeView,
)

urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="sign_up"),
    path("me/", UserMeView.as_view(), name="user_me"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh")
]