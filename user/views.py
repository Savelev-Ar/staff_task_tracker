from rest_framework.response import Response
from rest_framework import generics, filters, viewsets
from rest_framework.permissions import AllowAny
from user.models import User
from user.serializers import UserSerializer, BusyUserSerializer



class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class BusyUserViewSet(viewsets.ViewSet):
    """
    Запрашивает из БД список сотрудников и их задачи,
    отсортированный по количеству активных задач.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = BusyUserSerializer(queryset, many=True)
        serializer_data = sorted(serializer.data, key=lambda k: k['number_of_tasks'], reverse=True)
        return Response(serializer_data)
