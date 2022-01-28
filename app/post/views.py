from post.models import Post, Comment
from post.forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from post.forms import PostForm, AddCommentForm
from django.urls import reverse_lazy


# main page
def index(request):
    post = Post.objects.all().order_by('-created')
    return render(request, "index.html", {"post": post})


# post detail
def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    print(post.pk)
    author = request.user
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=author, post=post, text=form.cleaned_data["text"]
            )
            form = AddCommentForm()
            pass
    else:
        form = AddCommentForm()
    return render(request, 'post_detail.html', {'post': post, 'form': form})


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


# create new post
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
    # active_user = News.objects.get(author_id=request.user.pk)
    Post.objects.get(author_id=request.user.pk, id=post_pk).delete()
    return redirect('profile')


# удаление коментария по id. Может удалить только тот кто написал коментарий.
def delete_comment(request, comm_pk):
    author = request.user
    # получаем коментарий
    comment = Comment.objects.get(id=comm_pk)
    # получаем пост по ID через поле в связанной таблице (comment.post_id)
    object = Post.objects.get(id=comment.post_id)
    print(object)
    try:
        Comment.objects.get(id=comm_pk, author=author).delete()
    except:
        return redirect('no_permission')
    # Передавая объект; в качестве URL-а для перенаправления
    # будет использоваться результат вызова метода get_absolute_url()
    return redirect(object)


def no_permission(request):
    return render(request, 'no_permission.html')
