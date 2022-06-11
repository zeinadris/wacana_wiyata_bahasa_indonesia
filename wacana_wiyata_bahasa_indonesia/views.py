from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    context = {
        'judul' : 'Wacana Wiyata Bahasa Indonesia',
        'banner': 'img/home.jpg',
        'nav': [
            ['/','Home'],
            ['/blogs', 'Blogs'],
            ['/about', 'About']
        ]
    }
    return render(request, 'base.html', context)
    