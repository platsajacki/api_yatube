from rest_framework import serializers

from posts.models import Post, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date',
            'author', 'image', 'group'
        )
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'description')
        read_only_fields = ('slug',)
