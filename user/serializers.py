from rest_framework import serializers
from task.serializers import TaskSerializer
from user.models import User
from task.models import Task


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'last_name', 'middle_name', 'first_name', 'position']


class BusyUserSerializer(serializers.ModelSerializer):
    number_of_tasks = serializers.SerializerMethodField()
    tasks = serializers.SerializerMethodField()

    def get_number_of_tasks(self, user):
        return Task.objects.filter(executor=user).count() # status='accept').count()

    def get_tasks(self, user):
        tasks = Task.objects.filter(executor=user, status='accept')
        tasks_list = []
        for task in tasks:
            tasks_list.append(task.title)
        return tasks_list
    class Meta:
        model = User
        fields = ['email', 'tasks', 'number_of_tasks']
        ordering = ['-number_of_tasks']
