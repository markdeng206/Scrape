from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers


class BookListCreateViewSet(ListCreateAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()


class BookRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
