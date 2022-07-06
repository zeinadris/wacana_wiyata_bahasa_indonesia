from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):

    context ={
        'judul': 'Wacana Wiyata Bahasa Indonesia',
        'subjudul' : 'About Us',
        'desc_blogs' : 'Kelompok 7 Anggota : ',
        'desc_blogs1' : 'Ketua : Nayaka Nadhiftya Almas (210101075)',
        'desc_blogs2' : 'Quality Control : Zein Adri Saputro (210101087)',
        'desc_blogs3' : 'Content Writer : Krisna Febrianti (210101065)',
        'banner': 'about/img/about-2.jpg',
        'content' : 'img/logo-web.png',
        'nav' : [
            ['/','Home'],
            ['/list_blogs','Blog']
        ]
    }

    return render(request, 'base.html', context)
