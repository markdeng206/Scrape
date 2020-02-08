from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers


class NewsListCreateViewSet(ListCreateAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = models.News.objects.all()


class NewsRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.NewsSerializer
    queryset = models.News.objects.all()

