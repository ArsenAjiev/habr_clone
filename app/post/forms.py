from django import forms
from django.contrib.auth.forms import UserCreationForm
from post.models import Post
from datetime import date


#  new user registration form
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# add post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category', 'tags']
        exclude = ('author',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            # важно при загрузке изображения!!!
            'image': forms.FileInput(attrs={'class': 'input-image-control'})
        }


# add comment form
class AddCommentForm(forms.Form):
    text = forms.CharField(label="Введите коментарий", widget=forms.TextInput(attrs={'class': 'form-control'}))


# choice post
class ChoicePostForm(forms.Form):
    date_1 = forms.DateTimeField(label="Первая дата",
                                    initial=format(date),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_2 = forms.DateTimeField(label="Вторая дата",
                                 initial=format(date),
                                 widget=forms.widgets.DateInput(attrs={'type': 'date'}))