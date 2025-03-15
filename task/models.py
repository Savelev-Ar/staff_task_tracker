from django.db import models

from user.models import User

NULLABLE = {'blank': True, 'null': True}

class Task(models.Model):
    STATUS = (('active', 'активная'),
              ('accept', 'взята на исполнение'),
              ('complete', 'выполнена'),
              ('cancel', 'отклонена'),)

    title = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        help_text='Укажите наименование задачи')
    description = models.TextField(
        verbose_name='описание',
        help_text='опишите задачу',
        **NULLABLE)
    # ссылка на родительскую задачу (если есть зависимость)
    parent_task = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Связанная задача',
        help_text='Укажите связанную задачу',
        **NULLABLE)
    executor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='executor',
        verbose_name='исполнитель',
        **NULLABLE)
    deadline = models.DateField(
        verbose_name='Срок исполнения')
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default='active',
        verbose_name='статус задачи')
