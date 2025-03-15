from django.urls import path

from task.apps import TaskConfig

from task.views import (TaskCreateAPIView,
                        TaskListAPIView,
                        TaskRetrieveAPIView,
                        TaskUpdateAPIView,
                        TaskDestroyAPIView)

app_name = TaskConfig.name


urlpatterns = [
    path('task/create/', LessonCreateAPIView.as_view(), name='task-create'),
    path('task/', LessonListAPIView.as_view(), name='task-list'),
    path('task/<int:pk>/', LessonRetrieveAPIView.as_view(), name='task-get'),
    path('task/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='task-delete'),
]
