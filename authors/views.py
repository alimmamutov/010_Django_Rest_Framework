from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.renderers import AdminRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographySerializer, BookSerializer, ArticleSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name', 'last_name', 'birthday_year']
    # def get_queryset(self):  # фильтрация выборки
    #     name = self.request.query_params['name']
    #     headers = self.request.headers
    #     return Author.objects.filter(first_name__contains=name)



class BiographyModelViewSet(ModelViewSet):
    renderer_classes = [AdminRenderer]
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorViewSimpleResp(APIView):
    def get(self, request):
        return Response('Hello!!!! GET response')

    def post(self, request):
        return Response('POST response!!!!')


class AuthorViewSerResp(APIView):

    def get(self, request):
        authors = Author.objects.all()
        ser = AuthorModelSerializer(authors, many=True)
        return Response(ser.data)

    def post(self, request):
        return Response('POST response!!!!')


class AuthorListView(ListAPIView, CreateAPIView): # При множественном наследовании получается указать Доступные методы дженериков
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class AuthorViewSet(ViewSet):

    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])  # detail=False означает, что работаем с множеством объектов
    def change_password_ururu(self, request):
        return Response('My action')


class AuthorCustomModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]