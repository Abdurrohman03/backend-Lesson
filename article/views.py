from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, Http404, redirect, reverse
from .models import Article
import random
from .forms import ArticleForm
from django.contrib import messages


def __index(request):
    _id = random.randint(1, 3)
    obj = Article.objects.get(id=_id)
    title = obj.title
    content = obj.content
    HTML_CONTENT = f'''
    <h1>{title} (id: {obj.id}</h1>
    {content}
    '''
    return HttpResponse(HTML_CONTENT)


def index(request):
    articles = Article.objects.filter(is_deleted__exact=False).order_by('-id')
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    return render(request, 'article/index.html', {'object_list': articles})


def detail(request, slug=None):
    if slug:
        article = Article.objects.get(slug=slug)
        return render(request, 'article/detail.html', {'object': article})
    return Http404


def _create(request):
    context = {
        'created': False
    }
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        context['created'] = True
        context['object'] = article
        # return redirect(reverse('articles:detail', kwargs={'pk': article.id}))
    return render(request, 'article/create.html', context)


def __create(request):
    form = ArticleForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            context['object'] = form.data
            context['created'] = True

    return render(request, 'article/create.html', context)


def create(request):
    form = ArticleForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Article created')
        return redirect('articles:list')
    context = {
        'form': form
    }
    return render(request, 'article/create.html', context)


@login_required
def edit(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article, files=request.FILES)
        messages.success(request, f'Article updated ({article.id})')
        form.save()
        return redirect(reverse('articles:detail',  kwargs={'slug': article.slug}))
    ctx = {
        'form': form
    }
    return render(request, 'article/edit.html', ctx)


@login_required
def delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == "POST":
        article.is_deleted = True
        messages.success(request, f'Article deleted ({article.id})')
        article.save()
        return redirect('articles:list')
    context = {
        'object': article
    }
    return render(request, 'article/delete.html', context)
