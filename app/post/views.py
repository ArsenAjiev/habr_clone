from post.models import Post, Comment
from post.forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from post.forms import PostForm, AddCommentForm, ChoicePostForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator


# main page
def index(request):
    post = Post.objects.all().order_by('-created')
    paginator = Paginator(post, 3)
    page_number = request.GET.get("page")
    post = paginator.get_page(page_number)
    return render(request, "index.html", {"post": post})



# tag index view
class TagIndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(tags__pk=self.kwargs.get('tag_pk')).order_by('-created')



# post detail
def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
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
    post = Post.objects.all().order_by('-created')
    paginator = Paginator(post, 3)
    page_number = request.GET.get("page")
    post = paginator.get_page(page_number)
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
    success_url = reverse_lazy('profile')
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
    try:
        Comment.objects.get(id=comm_pk, author=author).delete()
    except:
        return redirect('no_permission')
    # Передавая объект; в качестве URL-а для перенаправления
    # будет использоваться результат вызова метода get_absolute_url()
    return redirect(object)


def no_permission(request):
    return render(request, 'no_permission.html')


def choice_date(request):
    choice_post = Post.objects.all()
    date_1 = []
    date_2 = []
    count_post = Post.objects.count()
    if request.method == 'POST':
        form = ChoicePostForm(request.POST)
        if form.is_valid():
            date_1 = form.cleaned_data["date_1"]
            date_2 = form.cleaned_data["date_2"]
            choice_post = choice_post.filter(created__range=[date_1, date_2]).order_by('-created')
            count_post = choice_post.count()
            form = ChoicePostForm()
            pass
    else:
        form = ChoicePostForm()
    context = {
        'choice_post': choice_post,
        'form': form,
        'date_1': date_1,
        'date_2': date_2,
        'count_post': count_post,
    }
    return render(request, 'choice_date.html', context)


def choice_category(request, name):
    # индексация поля в связанной модели с дополнительным двойным подчеркиванием
    posts = Post.objects.filter(category__title=name)
    num_posts = posts.count()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    return render(request, 'post_category.html', {'posts': posts, 'name': name, 'num_posts': num_posts})


def choice_post_title(request):
    query_dict = request.GET
    query = query_dict.get("q")
    post_search = None
    if query is not None:
        post_search = Post.objects.filter(title__contains=query) or Post.objects.filter(text__contains=query)
    count_post_search = post_search.count()
    context = {
        'post_search': post_search,
        'query': query,
        'count_post_search': count_post_search
    }
    return render(request, 'choice_post_title.html', context=context)