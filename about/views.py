from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):

    context ={
        'judul' : 'Abou Us',
        'banner': 'about/img/about-2.jpg',
        'nav' : [
            ['/','Home'],
            ['/blogs','Blog']
        ]
    }

    return render(request, 'base.html', context)
