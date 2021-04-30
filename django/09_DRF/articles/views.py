from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
def create_or_list_article(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_article(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(instance=article)
        return Response(data=serializer.data)
    if request.method == 'PUT':
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save(article=article)
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        article.delete()
        data = {
            'success':'True',
            'message': f'{article_pk}번 게시글이 삭제되었습니다'
        }
        return Response(data=data)