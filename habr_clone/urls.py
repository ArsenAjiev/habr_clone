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
from post.views import index, post_detail, profile, register
from django.conf import settings
from post.views import CreatePost, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('news_detail/<post_pk>/', post_detail, name='post_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/', register, name='register'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('delete_post/<post_pk>/', delete_post, name='delete_post'),


]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Server static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

