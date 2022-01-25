from post.models import Post, Comment
from post.forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from post.forms import PostForm
from django.urls import reverse_lazy


# main page
def index(request):
    post = Post.objects.all().order_by('-created')
    return render(request, "index.html", {"post": post})


# post detail
def post_detail(request, post_pk):
    post = Post.objects.get(id=post_pk)
    return render(request, 'post_detail.html', {'post': post})


# profile
def profile(request):
    post = Post.objects.all().filter(author=request.user.pk).order_by('-created')
    return render(request, "profile.html", {"post": post})


# register user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
        else:
            messages.error(request, "registration error")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register_user.html', {"form": form})


class CreatePost(CreateView):
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    raise_exception = True


   # добавляет в поле автор id текущего юзера автоматически
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        print(form.instance.author_id)
        return super(CreatePost, self).form_valid(form)


def delete_post(request, post_pk):
    #active_user = News.objects.get(author_id=request.user.pk)
    Post.objects.get(author_id=request.user.pk, id=post_pk).delete()
    return redirect('profile')