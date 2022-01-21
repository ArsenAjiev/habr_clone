from django.shortcuts import render
from post.models import Post, Comment
from post.forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect



# главная страница приложения.
def index(request):
    post = Post.objects.all()

    return render(request, "index.html", {"post": post})


 # полная информация о новости
def post_detail(request, post_pk):
    post = Post.objects.get(id=post_pk)
    comments = Comment.objects.get(id=post_pk)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


def profile(request):
    post = Post.objects.all()
    return render(request, "profile.html", {"post": post})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register_user.html', {"form": form})




