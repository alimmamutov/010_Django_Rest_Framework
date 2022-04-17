
# В этом модуле отрабатываем создание и обновление обычных объектов Python
import os

from rest_framework.exceptions import ValidationError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
import django
django.setup()
from ex import Author
from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        return instance

    def validate_birthday_year(self, value):
        if value < 0:
            raise serializers.ValidationError('incorrect birthday')

    def validate(self, attrs):
        if attrs['name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
            raise serializers.ValidationError(f"Пушкин родился не в {attrs['birthday_year']}")
        return attrs

# Создание
data = {
    "name": 'Alex',
    'birthday_year': 1900
}

ser = AuthorSerializer(data=data)
ser.is_valid()
author = ser.save()

# Обновление
data = {
    "name": 'New Alex',
    'birthday_year': 1900
}
ser = AuthorSerializer(instance=author, data=data)
ser.is_valid()
author = ser.save()
a = 0


# Ошибки сериализации
data = {
    "name": 'New Alex',
    'birthday_year': 'ljhgl'
}
ser = AuthorSerializer(instance=author, data=data)
ser.is_valid()
try:
    ser.is_valid(raise_exception=True)
except serializers.ValidationError as error:
    print(f'first exception {error.detail}')

# Ошибки сериализации  дате рождения
data = {
    "name": 'New Alex',
    'birthday_year': -1
}
ser = AuthorSerializer(instance=author, data=data)
try:
    ser.is_valid(raise_exception=True)
except serializers.ValidationError as error:
    print(f'second exception {error.detail}')

# Ошибки сериализации Собственный сериализатор
data = {
    "name": 'Пушкин',
    'birthday_year': 1799
}
ser = AuthorSerializer(data=data)
try:
    ser.is_valid(raise_exception=True)
except serializers.ValidationError as error:
    print(f'third exception {error.detail}')
