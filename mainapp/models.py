from uuid import uuid4

from django.db import models

# Create your models here.
from authapp.models import User


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    repository = models.URLField(max_length=128, blank=True, verbose_name='Ссылка на репозиторий')
    users = models.ManyToManyField(User, blank=True, verbose_name='Пользователи')

    def __str__(self):
        return self.name


class ToDo(models.Model):
    ACTIVE = 'A'
    CLOSED = 'C'
    STATUS_CHOICES = (
        (ACTIVE, 'Активная'),
        (CLOSED, 'Закрытая')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    text = models.TextField(verbose_name='Текст заметки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default=ACTIVE, verbose_name='Статус заметки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')