from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):

    context ={
        'judul': 'Wacana Wiyata Bahasa Indonesia',
        'subjudul' : 'Abou Us',
        'banner': 'about/img/about-2.jpg',
        'content' : 'img/logo-web.png',
        'nav' : [
            ['/','Home'],
            ['/blogs','Blog']
        ]
    }

    return render(request, 'base.html', context)
