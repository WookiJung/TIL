from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article_pk=article.pk)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/forms.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article':article,
        'comments': comments,
        'comment_form': comment_form,
        }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET','POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'articles/forms.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')

@require_POST
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)       
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article_pk = article.pk)
    else:
        comment_form = CommentForm()
    context = {
        'comment_form':comment_form,
        }
    return render(request, 'articles/detail.html', context)

def comments_delete(request, article_pk, comments_pk):
    comment = get_object_or_404(Comment, pk=comments_pk)
    comment.delete()
    return redirect('articles:detail', article_pk = article_pk)
    