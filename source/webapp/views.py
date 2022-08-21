from django.shortcuts import render
from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Article.objects.all()
    else:
        data = Article.objects.filter(status='moderated')
    context = {
        'articles': data
    }
    return render(request, 'index.html', context)


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        status = request.POST.get('status')
        article = Article.objects.create(title=title, text=text, author=author, status=status)
        context = {
            'article': article
        }
        return render(request, 'article_view.html', context)


def article_view(request):
    article_id = request.GET.get('pk')
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'article_view.html', context)
