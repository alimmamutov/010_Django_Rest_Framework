from uuid import uuid4

from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, db_index=True)
    id = models.UUIDField(primary_key=True, default=uuid4)

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
