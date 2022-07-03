from django.shortcuts import render
# Create your views here.
from . models import Post


def homepage(request):
    all_posts = Post.newmanager.all()
    return render(request, 'index.html', {'posts': all_posts})


def single(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, 'single.html', {'singledata': data})


def aboutus(request):
    return render(request, 'aboutus.html')
