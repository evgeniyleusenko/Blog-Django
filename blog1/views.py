from django.shortcuts import render
# from django.http import HttpResponse

from .models import Post
# Create your views here.


def posts_list(request):
    posts=Post.objects.all()
    # posts={'a':1,'b':2}
    return render(request, 'blog1/index.html', context={'posts': posts})

def post_detail(request,slug):
    post=Post.objects.get(slug__iexact=slug)
    return render(request,'blog1/post_detail.html',context={'post': post})