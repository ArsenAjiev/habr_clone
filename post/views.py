from django.shortcuts import render
from post.models import Post, Comment
from django.http import HttpResponse
from django.core.cache import cache



# главная страница приложения.
def index(request):
    post = Post.objects.all()

    return render(request, "index.html", {"post": post})


 # полная информация о новости
def post_detail(request, post_pk):
    post = Post.objects.get(id=post_pk)
    comments = Comment.objects.get(id=post_pk)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})






