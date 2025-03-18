from django.urls import path
from rest_framework.routers import DefaultRouter
from task.apps import TaskConfig

from task.views import (TaskCreateAPIView,
                        TaskListAPIView,
                        TaskRetrieveAPIView,
                        TaskUpdateAPIView,
                        TaskDestroyAPIView,
                        ImportantTaskViewSet,
                        BusyUserViewSet)

app_name = TaskConfig.name

router = DefaultRouter()
router.register(r'important', ImportantTaskViewSet, basename='important')
router.register(r'busy', BusyUserViewSet, basename='busy-user')

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('', TaskListAPIView.as_view(), name='task-list'),
    path('<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-get'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task-delete'),
] + router.urls
