from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ContactForm, AriticleForm

def contact(request):  
    if request.method == 'GET':
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'articles/contact.html', context)
    elif request.method == 'POST':
        contact_form = ContactForm(request.POST)
        return redirect('contact')

def new(request):  # 뉴랑 크리에이트가 한꺼번에 묶여져있어.
    if request.method == 'POST':
        form = AriticleForm(request.POST)
        if form.is_valid:
            article = form.save()
            return redirect('articles:detail', article_pk = article.pk)
    else:
        form = AriticleForm()
    context = {'form': form}
    return render(request, 'articles/new.html', context)

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)  # article이 있는거 맞아?
    if request.method == 'POST':
        #  new와 다르게 특정 article에 대한 내용을 request.post로 덮어쓰겠다는 뜻!
        form = AriticleForm(request.POST, instance=article)
        if form.is_valid:
            article = form.save()
            return redirect('articles:detail', article_pk = article.pk)
    else:  # article은 인스턴스야. data는 only request일때만.
        # 기존게시글을 포함한 HTML을 만들기위해 instance 추가.
        form = AriticleForm(instance=article)
    context = {'form': form}
    return render(request, 'articles/edit.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk= article_pk)
    article.delete()
    return redirect('articles:index')

