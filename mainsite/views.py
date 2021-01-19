from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()

    # 把變數丟到模板去，使用locals()函數
    # locals()函數，會將記憶體中的區域變數用字典型態打包起來
    return render(request, 'index.html', locals())


def homepageAvoidError(request, slug):
    # 避免有人在首頁後輸入非Post的字，都將其導向到首頁
    posts = Post.objects.all()
    now = datetime.now()

    # 把變數丟到模板去，使用locals()函數
    # locals()函數，會將記憶體中的區域變數用字典型態打包起來
    try:
        if slug != None:
            return render(request, 'index.html', locals())
    except:
        return redirect('/')


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')
