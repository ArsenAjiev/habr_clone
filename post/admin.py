from django.contrib import admin
from post.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "created")
    fields = ("author", "text",)
    readonly_fields = ("created",)
    search_fields = ("text", )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "content_type", "object_id")
    fields = ("author", "text", "content_type", "object_id")
    search_fields = ("text",)
