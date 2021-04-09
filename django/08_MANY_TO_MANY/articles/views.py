from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Article.views

User = get_user_model()

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html',context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    context = {'article':article}
    return render(request, 'articles/detail.html', context)


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/form.html', context)
@login_required
def like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    article.like_users.add(user)
    return redirect('articles:index')
    
@login_required
def cancel_like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    article.like_users.remove(user)
    return redirect('articles:index')

