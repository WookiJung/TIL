from django.db import models
from django.conf import settings


# Article.models
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'dislikes')

    def __str__(self):
        return f'{self.pk} : {self.title}'
    
