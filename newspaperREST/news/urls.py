from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
    path('users/', views.ListCreateUsers.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
