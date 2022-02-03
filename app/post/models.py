from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Comment(models.Model):
    class Meta:
        ordering = ['-created']

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.text


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='category')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title
