from django.urls import path
from .views import ArticleView_using_APIView, ArticleView_using_GenericAPIView, SingleArticleView

app_name = 'articles'

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView_using_APIView.as_view()),
    path('articles/<int:pk>', ArticleView_using_APIView.as_view()),
    path('articles_generic/', ArticleView_using_GenericAPIView.as_view()),
    path('articles_generic/<int:pk>', SingleArticleView.as_view()),
]