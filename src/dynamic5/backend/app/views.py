from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers

class BookListCreateViewSet(ListCreateAPIView):
    serializer_class = serializers.BookIndexSerializer
    queryset = models.Book.objects.all()

class BookRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookDetailSerializer
    queryset = models.Book.objects.all()

class CommentListCreateViewSet(ListCreateAPIView):
    serializer_class = serializers.CommentIndexSerializer
    queryset = models.Comment.objects.all()

class CommentRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CommentDetailSerializer
    queryset = models.Comment.objects.all()
