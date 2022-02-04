from taggit.models import Tag
from post.models import Post


def tags_context_processor(request):
    context = {}
    #  context['tags'] = Tag.objects.all()
    context['most_comm_tags'] = Post.tags.most_common()[:10]
    return context
