from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, StringRelatedField

from .models import Author, Article, Biography, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['first_name']

# class AuthorModelSerializer(ModelSerializer):
#
#     class Meta:
#         model = Author
#         fields = ['__all__']


class BiographySerializer(ModelSerializer):
    author = AuthorModelSerializer() # Такой сериализатор выведет в виде словаря, с полями, указанными в fields AuthorModelSerializer
    # author = StringRelatedField()  # Такой сериализатор выведет в том виде, который указан в __str__ в модели

    class Meta:
        model = Biography
        fields = ['text', 'author']
        # fields = ['__all__']


class ArticleSerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        exclude = ['name']


class BookSerializer(ModelSerializer):
    authors = StringRelatedField(many=True)
    # authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
