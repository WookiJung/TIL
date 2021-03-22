from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to='article/',
        blank = True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality' : 90,}
        )  
    # blank=True는 ORM이 빈것을 허용하게 만든다는 뜻. ''일때 is_valid=True라 인식.
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)