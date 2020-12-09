from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ArticleView_using_APIView, ArticleView_using_GenericAPIView, SingleArticleView, ArticleViewSet

app_name = 'articles'

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView_using_APIView.as_view()),
    path('articles/<int:pk>', ArticleView_using_APIView.as_view()),
    path('articles_generic/', ArticleView_using_GenericAPIView.as_view()),
    path('articles_generic/<int:pk>', SingleArticleView.as_view()),
    # path('articles_viewSet/', ArticleView_using_ViewSet.as_view({'get': 'list'})),
    # path('articles_viewSet/<int:pk>', ArticleView_using_ViewSet.as_view({'get': 'retrieve'})),
]

router = DefaultRouter()
router.register(r'articles_viewSet', ArticleViewSet, basename='user')
urlpatterns += router.urls