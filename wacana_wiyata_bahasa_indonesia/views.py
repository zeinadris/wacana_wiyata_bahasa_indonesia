from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    context = {
        'judul' : 'Wacana Wiyata Bahasa Indonesia',
        'desc_blogs' : 'Wacana Wiyata Bahasa Indonesia adalah salah satu blog pembelajaran terkemuka di Indonesia dan Asia Tenggara. Deskripsi blog yang ditulis oleh Wacana Wiayata Bahasa Indonesia menunjukkan kalau mereka memang merupakan situs yang berpusat pada pendidikan dan kebasaan, mulai dari daftar blog, materi, deskripsi, judul, dan juga segala hal yang berkaitan dengan Bahasa Indonesia.',
        'subjudul': 'Home',
        'banner': 'img/home.jpg',
        'content' : 'img/logo-web.png',
        'nav': [
            ['/','Home'],
            ['/list_blogs', 'Blogs'],
            ['/about', 'About']
        ]
    }
    return render(request, 'base.html', context)
    