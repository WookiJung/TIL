from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content_a = models.CharField(max_length=100)
    content_b = models.CharField(max_length=100)
    class Content(models.TextChoices):
        choice_a = Article.content_a, _('A')
        choice_b = Article.content_b, _('B')
    
    choices = models.CharField(max_length=100, choices=Content.choices, )


class Comment(models.Model):
    content = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)