from rest_framework.renderers import AdminRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Author, Biography, Book, Article
from .serializers import AuthorModelSerializer, BiographySerializer, BookSerializer, ArticleSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


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