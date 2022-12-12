from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        queryset=User.objects, slug_field='username'
    )
    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        fields = ('__all__')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects,
                fields=['following', 'user']
            )
        ]
