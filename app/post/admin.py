from django.contrib import admin
from post.models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created", "image", "category", "tags")
    fields = ("author", "title", "text", "image", "category", "tags")
    readonly_fields = ("created",)
    search_fields = ("text",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "post")
    fields = ("author", "text", "post")
    search_fields = ("text",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
