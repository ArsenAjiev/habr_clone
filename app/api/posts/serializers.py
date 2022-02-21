from rest_framework import serializers
from post.models import Post
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'
