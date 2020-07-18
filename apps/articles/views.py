from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Article
from django.template.loader import render_to_string
import json


def article_for_day(request):
    context = {
        'articles': Article.objects.get_for_day(),
        'title': 'Статьи за день',
    }
    return render(request, 'articles/article_list.html', context)


def article_for_week(request):
    context = {
        'articles': Article.objects.get_for_week(),
        'title': 'Статьи за неделю',
    }
    return render(request, 'articles/article_list.html', context)


def article_for_all(request):
    context = {
        'articles': Article.objects.get_for_all(),
        'title': 'Все статьи',
    }
    if request.GET.get('mode'):
        data = {
            'html': render_to_string('articles/article_list.html', context)
        }
        data = json.dumps(data, ensure_ascii=False).replace('/', r'\/')
        return HttpResponse(data, content_type='application/json')
    return render(request, 'articles/article_list.html', context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'


# Create your views here.
