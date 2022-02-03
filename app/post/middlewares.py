from taggit.models import Tag


def tags_context_processor(request):
    context = {}
    context['tags'] = Tag.objects.all()
    return context
