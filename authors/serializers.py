from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from .models import Author, Article, Biography, Book


# class AuthorModelSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['__all__']


class BiographySerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        exclude = ['name']


class BookSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'
