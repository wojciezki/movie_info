from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from url_filter.integrations.drf import DjangoFilterBackend

from ..models import Comment
from ..serializers import CommentBaseSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    serializers = {
        'default': CommentBaseSerializer,
    }
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('movie',)
    ordering_fields = ('movie',)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])
