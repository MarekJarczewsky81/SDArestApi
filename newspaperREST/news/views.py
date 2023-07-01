from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def list_create_articles(request, format=None):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, articleId, format=None):
    # try:
    #     article = Article.objects.get(id=articleId)
    # except Article.DoesNotExist:
    #     return Response({'Error': f'Article with id {articleId} was not found.'},status=status.HTTP_404_NOT_FOUND)
    article = get_object_or_404(Article, id=articleId)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
