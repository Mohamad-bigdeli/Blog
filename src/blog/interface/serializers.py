from rest_framework import serializers
from ..infrastructure.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id", 
            "title",
            "description",
            "created",
            "updated",
        ]
        read_only_fields = ["id", "created", "updated"]