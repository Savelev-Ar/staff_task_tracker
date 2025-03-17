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

    def test_create_user(self):
        self.data = {
            "email": "test2@email.ru",
            "password": "testword",
            "position": "middle",
            "first_name": "Имя",
            "middle_name": "Отчество",
            "last_name": "Фамилия"
        }
        url = reverse('user:register')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list(self):
        url = reverse('user:users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        url = reverse('user:user-delete', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Exception):
            User.objects.get(pk=self.user.pk)

    def test_update_user(self):
        url = reverse('user:user-update', kwargs={"pk": self.task.pk})
        self.data = {"last_name": "Да фамилия"}
        response = self.client.patch(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_busy_user_list(self):
        url = reverse('user:user-busy')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
