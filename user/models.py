from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Электропочта',
        help_text='Укажите свою электрическую почту')
    first_name = models.CharField(
        max_length=50,
        verbose_name='И',
        help_text='Укажите своё имя')
    middle_name = models.CharField(
        max_length=50,
        verbose_name='О',
        help_text='Укажите свое отчество')
    last_name = models.CharField(
        max_length=50,
        verbose_name='Ф',
        help_text='Укажите свою фамилию')

    position = models.CharField(
        max_length=100,
        verbose_name='Должность пользователя',
        help_text='Укажите свою должность')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['position']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']
