from rest_framework import serializers
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

# print(serializer_first.data)
# print (serializer_second.data)
# print(serializer_third.data)
print(general.data)
