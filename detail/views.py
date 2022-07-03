from multiprocessing import context
from turtle import bye
from django.shortcuts import render
from list_blogs.models import ListBlog

# Create your views here.
def index(request):
    blogid = request.GET.get('id', '')
    blogs = ListBlog.objects.get(id = blogid)
    context = {
        'judul' : 'Wacana Wiyata Bahasa Indonesia',
        'subjudul' : 'Detail Blog',
        'banner': 'detail/img/detail.jpg',
        'content': 'img/logo-web.png',
        'blog': blogs,
        'nav' : [
            ['/','Home'],
            ['/about','About'],
            ['/list_blogs', 'Blogs'],
        ]
    }
    return render(request, 'base.html', context)
