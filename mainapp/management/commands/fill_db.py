import json
import random

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from authapp.models import User
from mainapp.models import Project, ToDo


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Project.objects.all().delete()
        ToDo.objects.all().delete()

        # Add superuser
        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser(username='django', email='admin@service.local', password='geekbrains')

        # Add simple users
        simple_users = load_from_json('mainapp/fixtures/users.json')
        for user in simple_users:
            user['password'] = make_password('geekbrains')
            new_user = User(**user)
            new_user.save()

        # Add projects
        projects = load_from_json('mainapp/fixtures/projects.json')
        for project in projects:
            user_list = list(User.objects.exclude(username='django'))
            new_proj = Project(**project)
            new_proj.save()
            new_proj.users.add(*user_list)

            # Add ToDoes
            random.shuffle(user_list)
            for user in user_list[0:2]:
                _todo = {
                    'user': user,
                    'project': new_proj,
                    'text': f'Заметка пользователя {user}'
                }
                new_todo = ToDo(**_todo)
                new_todo.save()
