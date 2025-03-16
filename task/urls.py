from django.urls import path

from task.apps import TaskConfig

from task.views import (TaskCreateAPIView,
                        TaskListAPIView,
                        TaskRetrieveAPIView,
                        TaskUpdateAPIView,
                        TaskDestroyAPIView)

app_name = TaskConfig.name


urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('', TaskListAPIView.as_view(), name='task-list'),
    path('<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-get'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task-delete'),
]
