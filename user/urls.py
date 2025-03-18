from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from user.apps import UserConfig
from user.views import (UserCreateAPIView,
                        UserListAPIView,
                        UserRetrieveAPIView,
                        UserUpdateAPIView,
                        UserDestroyAPIView)

app_name = UserConfig.name


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token-refresh'),
    path('', UserListAPIView.as_view(), name='users'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]
