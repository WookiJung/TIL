from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST, require_GET, require_http_methods

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'boards/index.html', context)

@require_http_methods(['GET','POST'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('boards:index')
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'boards/form.html', context)

def detail_article(request,article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article' : article,
        'comment_form':comment_form,
        'comments':comments
    }
    return render(request, 'boards/detail.html', context)

def update_article(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', article.pk)
    else:
        form = ArticleForm(instance = article)
    context = {
        'form':form
    }
    return render(request, 'boards/form.html', context)

@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('boards:index')

@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('boards:detail', article_pk=article.pk)
    else:
        comment_form = CommentForm()
    context = {
        'comment_form':comment_form,
    }
    return render(request, 'boards/detail.html', context)

@require_POST
def delete_comment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('boards:detail', article_pk=article_pk)