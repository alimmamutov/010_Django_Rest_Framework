
# В этом модуле отрабатываем создание и обновление обычных объектов Python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
import django
django.setup()
from authors.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ['birthday_year']

    # def create(self, validated_data):
    #     return Author(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
    #     return instance


# Создание
data = {
    "last_name": 'Pushkin',
    'first_name': 'Aleksandr',
    'birthday_year': 1900
}

ser = AuthorSerializer(data=data)
ser.is_valid(raise_exception=True)
author = ser.save()

# author = Author.objects.create(**data)
# serializer = AuthorSerializer(author)


