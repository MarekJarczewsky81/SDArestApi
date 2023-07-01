from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view()),
    path('articles/<int:articleId>/', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
