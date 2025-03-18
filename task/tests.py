from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from django.utils import timezone
from django.urls import reverse

from task.models import Task
from user.models import User


class TaskDeleteTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@email.ru',
            position='junior')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(
            title='опиши модель',
            deadline=timezone.now().date())

    def test_create_task(self):
        self.data = {
            "title": 'опиши CRUD модели',
            "deadline": timezone.now().date(),
            "executor": self.user.pk
        }
        url = reverse('task:task-create')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list(self):
        url = reverse('task:task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        url = reverse('task:task-delete', kwargs={'pk': self.task.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Exception):
            Task.objects.get(pk=self.task.pk)

    def test_update_task(self):
        url = reverse('task:task-update', kwargs={"pk": self.task.pk})
        self.data = {"description": "описать модели User и Task"}
        response = self.client.patch(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_busy_user_list(self):
        url = '/task/busy/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
