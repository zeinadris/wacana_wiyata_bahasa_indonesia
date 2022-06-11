from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from . models import Blog

def index(request):
    blogs = Blog.objects.all()
    context = {
        'judul' : 'Wacana Wiyata Bahasa Indonesia',
        'subjudul' : 'Blog',
        'banner': 'blog/img/blog.jpg',
        'nav' : [
            ['/','Home'],
            ['/about','About']
        ]
    }
    return render(request, 'base.html', context)
    