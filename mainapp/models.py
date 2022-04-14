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
