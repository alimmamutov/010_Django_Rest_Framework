import json
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from authapp.models import User
from mainapp.models import Article


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Article.objects.all().delete()
        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser(username='django', email='admin@service.local', password='geekbrains')

        simple_users = load_from_json('authapp/fixtures/users.json')
        for user in simple_users:
            user['password'] = make_password('geekbrains')
            new_user = User(**user)
            new_user.save()

            new_article = Article(
                name = 'Статья 1',
                text = 'Текст статьи 2',
                user = new_user
            )
            new_article.save()

