from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


class ListCreateArticles(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get(self, request, articleId):
        article = get_object_or_404(Article, id=articleId)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, articleId):
        article = get_object_or_404(Article, id=articleId)
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, articleId):
        article = get_object_or_404(Article, id=articleId)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
