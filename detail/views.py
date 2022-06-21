from multiprocessing import context
from turtle import bye
from django.shortcuts import render
from blogs.models import Blog

# Create your views here.
def index(request):
    blogid = request.GET.get('id', '')
    blogs = Blog.objects.get(id = blogid)
    context = {
        'judul' : 'Wacana Wiyata Bahasa Indonesia',
        'subjudul' : 'Blog',
        'banner': 'blog/img/blog.jpg',
        'content': 'img/logo-web.png',
        'blog': blogs,
        'nav' : [
            ['/','Home'],
            ['/about','About'],
            ['/blogs', 'Blogs'],
        ]
    }
    return render(request, 'base.html', context)
