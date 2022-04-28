"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, BiographyModelViewSet, BookModelViewSet, ArticleModelViewSet, AuthorViewSimpleResp, AuthorViewSerResp
import authors.views as AuthorsViews
from authapp.views import UserModelViewSet
from mainapp.views import ArticleAPIVIew, article_view

router = DefaultRouter()
router.register('authors_model_viewset', AuthorModelViewSet)
# router.register('biography', BiographyModelViewSet)
# router.register('articles', ArticleModelViewSet)
# router.register('books', BookModelViewSet)
# router.register('article_class_view', ArticleAPIVIew)
# router.register('article_func_view', article_view)
router.register('test', AuthorsViews.AuthorViewSet,basename='test')
router.register('authors', AuthorsViews.AuthorCustomModelViewSet, basename='authors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('views/api-view-class/', ArticleAPIVIew.as_view()),
    path('views/api-view-func/', article_view),
    path('views/testview_simple_response', AuthorViewSimpleResp.as_view()),
    path('views/testview_ser_response', AuthorViewSerResp.as_view()),
    path('views/testview_list_view', AuthorsViews.AuthorListView.as_view()),
]
