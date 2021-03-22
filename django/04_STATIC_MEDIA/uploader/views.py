from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.Files)
        if form.is_valid():
            article = form.save()
            return redirect('uploader:detail', article.pk)
    else:
        form = ArticleForm()
    context ={'form':form}
    return render(request, 'uploader/forms.html', context)


def index(request):

    return render(request, 'uploader/index.html')


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article':article}
    return render(request, 'uploader/detail.html', context)
