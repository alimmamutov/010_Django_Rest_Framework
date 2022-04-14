# Generated by Django 4.0.3 on 2022-04-14 10:59

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('repository', models.URLField(blank=True, max_length=128, verbose_name='Ссылка на репозиторий')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
        ),
    ]
