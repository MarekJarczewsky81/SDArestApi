from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.


class ListCreateArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
