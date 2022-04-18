
# В этом модуле отрабатываем создание и обновление обычных объектов Python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
import django
django.setup()
from authors.models import Author, Article, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ['birthday_year']

    # def create(self, validated_data):
    #     validated_data['first_name'] = f"{validated_data.get('first_name', validated_data['first_name'])} Изменено"
    #     return Author(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
    #     return instance


# Создание
# data = {
#     "last_name": 'Pushkin',
#     'first_name': 'Aleksandr',
#     'birthday_year': 1900
# }

# ser = AuthorSerializer(data=data)
# ser.is_valid(raise_exception=True)
# author = ser.save()
# author.save()
# a = 0

# author = Author.objects.create(**data)
# serializer = AuthorSerializer(author)


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = '__all__'


a1 = Article.objects.all()[0]
ser = ArticleSerializer(instance=a1)
print(ser.data)


class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True)
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'

b1 = Book.objects.all()[0]
ser = BookSerializer(b1)
print(ser.data)