from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    context = {
        'judul' : 'Wacana Wiyata Bahasa Indonesia',
        'subjudul': 'Home',
        'banner': 'img/home.jpg',
        'content' : 'img/logo-web.png',
        'nav': [
            ['/','Home'],
            ['/blogs', 'Blogs'],
            ['/about', 'About']
        ]
    }
    return render(request, 'base.html', context)
    