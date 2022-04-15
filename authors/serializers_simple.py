import io
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")

import django
django.setup()

from django.core.management import call_command

from rest_framework import serializers, settings
from rest_framework.renderers import JSONRenderer
# from rest_framework.renderers import JSONRenderer

from ex import Author, Biography, Book, Article


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()


class BiographySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=128)
    author = AuthorSerializer()


class GeneralAuthorSerializer(serializers.Serializer):
    author = AuthorSerializer()
    bio = BiographySerializer()


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    authors = AuthorSerializer(many=True)






author_first = Author('Грин', 1880)
author_second = Author('Пушкин', 1500)
biography_first = Biography('My text', author_first)
book_first = Book('Test book', [author_first, author_second])

serializer_first = AuthorSerializer(author_first)
serializer_second = BiographySerializer(biography_first)
serializer_third = BookSerializer(book_first)
general = GeneralAuthorSerializer(author_first)

print(serializer_first.data)
# print (serializer_second.data)
# print(serializer_third.data)
# print(general.data)

json_renderer = JSONRenderer()
json_bytes = json_renderer.render(serializer_first.data)
print(json_bytes)
print(type(json_bytes))

# Обратное преобразование из байтов в словарь
from rest_framework.parsers import JSONParser
stream = io.BytesIO(json_bytes)
data = JSONParser().parse(stream)
print(data) # {'name': 'Грин', 'birthday_year': 1880}
print(type(data)) # <class 'dict'>

# Преобразование словаря в сериализатор
serializer_last = AuthorSerializer(data=data)
print(serializer_last.is_valid())
print (serializer_last.validated_data)

# Преобразование сериализатора в объект
author_last = Author(**serializer_last.validated_data)
print(author_last)
