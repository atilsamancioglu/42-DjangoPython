from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post

# Create your views here.

def postIndex(request):
    posts = Post.objects.all()
    return render(request, 'post/index-post.html', {'posts':posts})

def postDetail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/detail-post.html', {'posts':post})

def postDelete(request):
    return HttpResponse('<center><h1>Post Delete</h1></center>')

def postCreate(request):
    return HttpResponse('<center><h1>Post Create</h1></center>')

def postUpdate(request):
    return HttpResponse('<center><h1>Post Update</h1></center>')