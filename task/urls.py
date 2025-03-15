from django.urls import path

from task.apps import TaskConfig

from task.views import (TaskCreateAPIView,
                        TaskListAPIView,
                        TaskRetrieveAPIView,
                        TaskUpdateAPIView,
                        TaskDestroyAPIView)

app_name = TaskConfig.name


urlpatterns = [
    path('task/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('task/', TaskListAPIView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-get'),
    path('task/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task-delete'),
]
