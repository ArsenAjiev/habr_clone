from django.urls import path
from news.views import news


urlpatterns = [
    path('', news, name='news')
]