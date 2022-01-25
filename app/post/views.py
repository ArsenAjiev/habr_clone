from post.models import Post, Comment
from post.forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from post.forms import PostForm, AddCommentForm
from django.urls import reverse_lazy
from django.contrib.contenttypes.models import ContentType



# main page
def index(request):
    post = Post.objects.all().order_by('-created')
    return render(request, "index.html", {"post": post})


# post detail
def post_detail(request, post_pk):
    post = Post.objects.get(id=post_pk)
    # Принимает либо класс модели, либо экземпляр модели и возвращает экземпляр ContentType представляющий эту модель.
    obj_type = ContentType.objects.get_for_model(Post)
    # ID конкретного поста
    object_id = post_pk
    # текущий пользователь в системе
    author = request.user
    # вывел в консоль что бы посмотреть значения
    print(obj_type, object_id, author)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                content_type=obj_type, object_id=object_id, author=author, text=form.cleaned_data["text"]
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


# удаление коментария по id. Может удалить только тот кто написал коментарий.
# в дальнейшем попробую вывести сообщение на странице.
def delete_comment(request, comm_pk):
    comment_id = comm_pk
    author = request.user
    try:
        Comment.objects.get(id=comment_id, author=author).delete()
    except:
        print("У Вас нет прав на удаления комментария")
    return redirect('profile')
