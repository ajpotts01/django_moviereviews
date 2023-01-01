from django.http import HttpRequest
from django.shortcuts import render

from .models import News

def news(request: HttpRequest):
    news_posts = News.objects.all().order_by('-date')

    return render(request, 'news.html', {
        'news_posts': news_posts
    })