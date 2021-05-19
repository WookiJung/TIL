from accounts.models import User
from django.db.models import fields
from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at',)

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False) # is_valid 검증 X
    class Meta:
        model = Article
        fields = '__all__'