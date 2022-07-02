from django.shortcuts import render
from . models import ListBlog

def index(request):
    blogs = ListBlog.objects.all()
    context = {
        'judul' : 'Wacana Wiyata Bahasa Indonesia',
        'subjudul' : 'Daftar Blog',
        'banner': 'list-blogs/img/blog.jpg',
        'logo' : 'list-blogs/img/logo.jpg',
        'content' : 'img/logo-web.png',
        'blogs': blogs,
        'nav' : [
            ['/','Home'],
            ['/about','About']
        ]
    }
    return render(request, 'base.html', context)
    