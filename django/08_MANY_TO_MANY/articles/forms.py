from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(min_length=1)
    class Meta:
        model = Article
        fields = ('title', 'content',)