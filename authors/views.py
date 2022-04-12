from rest_framework.viewsets import ModelViewSet
from .models import Author, Biography
from .serializers import AuthorModelSerializer, BiographySerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
