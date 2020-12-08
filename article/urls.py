from django.urls import path
from .views import ArticleView_using_APIView


app_name = 'articles'

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView_using_APIView.as_view()),
    path('articles/<int:pk>', ArticleView_using_APIView.as_view()),
]