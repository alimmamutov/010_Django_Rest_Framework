import json
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from authapp.models import User
from mainapp.models import Project


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Project.objects.all().delete()

        # Add superuser
        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser(username='django', email='admin@service.local', password='geekbrains')

        # Add simple users
        simple_users = load_from_json('authapp/fixtures/users.json')
        for user in simple_users:
            user['password'] = make_password('geekbrains')
            new_user = User(**user)
            new_user.save()

        # Add projects
        projects = load_from_json('authapp/fixtures/projects.json')
        for project in projects:
            proj = project.get('fields')
            # current_user = User.objects.get(id=proj.get('user'))
            # prod['user'] = current_user
            new_proj = Project(**proj)
            new_proj.save()