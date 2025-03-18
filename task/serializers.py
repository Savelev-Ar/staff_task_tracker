from rest_framework import serializers
from task.models import Task
from user.models import User


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class ExecutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name']


class BusyUserSerializer(serializers.ModelSerializer):
    number_of_tasks = serializers.SerializerMethodField()
    tasks = serializers.SerializerMethodField()

    def get_number_of_tasks(self, user):
        return Task.objects.filter(executor=user, status='accept').count()

    def get_tasks(self, user):
        tasks = Task.objects.filter(executor=user, status='accept')
        tasks_list = []
        for task in tasks:
            tasks_list.append(task.title)
        return tasks_list

    class Meta:
        model = User
        fields = ['email', 'tasks', 'number_of_tasks']


class ImportantTaskSerializer(serializers.ModelSerializer):
    """
       1. Запрашивает из БД задачи, которые не взяты в работу, но от которых зависят другие задачи, взятые в работу.
       2. Реализует поиск по сотрудникам, которые могут взять такие задачи (наименее загруженный сотрудник или
        сотрудник, выполняющий родительскую задачу, если ему назначено максимум на 2 задачи больше, чем у наименее
         загруженного сотрудника).
       3. Возвращает список объектов в формате: `{Важная задача, Срок, [ФИО сотрудника]}`.
    """
    available_executors = serializers.SerializerMethodField()

    @staticmethod
    def get_min_task_user(task):
        # юзер с наименьшим количеством задач
        executors = User.objects.all()
        user_tasks = {}
        for user in executors:
            user_tasks[user] = Task.objects.filter(executor=user, status='accept').count()
        sorted_user_task = sorted(user_tasks.items(), key=lambda item: item[1])
        min_task_user, task_count = sorted_user_task[0]
        return min_task_user, task_count

    def get_available_executors(self, task):
        # ищем важные задачи, выставляем признак важности
        parent_task_executor_task_count = 0
        if task.status == 'active' and task.parent_task is not None:
            parent_task = Task.objects.get(id=task.parent_task.id)
            if parent_task.status == 'accept':
                task.is_important = True
                parent_task_executor = parent_task.executor
                parent_task_executor_task_count = Task.objects.filter(executor=parent_task_executor,
                                                                      status='accept').count()
            else:
                task.is_important = False
            task.save()
        # ищем наименеее загруженных
        available_executor, available_executor_task_count = ImportantTaskSerializer.get_min_task_user(task)
        if parent_task_executor_task_count != 0:
            if available_executor_task_count+2 < parent_task_executor_task_count:
                result = available_executor
            else:
                result = parent_task_executor
        else:
            result = available_executor
        return ExecutorSerializer(result).data

    class Meta:
        model = Task
        fields = (
            'title',
            'deadline',
            'available_executors'
        )
