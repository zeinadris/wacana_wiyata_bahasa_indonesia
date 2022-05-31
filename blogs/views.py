from django.http import HttpResponse
from django.shortcuts import render
from . models import Blog

def index(request):
    blogs = Blog.objects.all()
    output = ', '.join([str(blog) for blog in blogs])
    return HttpResponse(output)