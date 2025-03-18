from rest_framework import generics, viewsets
from rest_framework.response import Response
from task.models import Task
from user.models import User
from task.serializers import TaskSerializer, ImportantTaskSerializer, BusyUserSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ImportantTaskViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Task.objects.filter(status='active', is_important=True)
        serializer = ImportantTaskSerializer(queryset, many=True)
        return Response(serializer.data)


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
