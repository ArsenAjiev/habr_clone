"""habr_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from post.views import index, post_detail, profile, register
from post.views import CreatePost, delete_post, delete_comment, no_permission

urlpatterns = [

    path('', index, name='home'),
    path('post_detail/<post_pk>/', post_detail, name='post_detail'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('delete_post/<post_pk>/', delete_post, name='delete_post'),
    path('delete_comment/<comm_pk>/', delete_comment, name='delete_comment'),
    path('no_permission/', no_permission, name='no_permission'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
