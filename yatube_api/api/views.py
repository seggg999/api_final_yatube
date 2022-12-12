from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import serializers

from .permissions import IsAutherOrReadOnly
from posts.models import Post, Group, Comment, Follow
from .serializers import (PostSerializer, GroupSerializer, CommentSerializer,
                          FollowSerializer
                          )


class CreateListModeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet
                            ):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAutherOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        super(PostViewSet, self).perform_create(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAutherOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAutherOrReadOnly,)

    def get_queryset(self):
        queryset = self.queryset.filter(post_id=self.kwargs['post_id'])
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        super(CommentViewSet, self).perform_create(serializer)


class FollowViewSet(CreateListModeViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        if serializer.validated_data.get('following') == self.request.user:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        super(FollowViewSet, self).perform_create(serializer)
