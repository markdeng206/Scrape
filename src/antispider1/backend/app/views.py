from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers


class MovieListCreateViewSet(ListCreateAPIView):
    serializer_class = serializers.MovieIndexSerializer
    queryset = models.Movie.objects.all()


class MovieRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieDetailSerializer
    queryset = models.Movie.objects.all()

