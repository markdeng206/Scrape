from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models
from . import serializers
from django.core.paginator import Paginator


class MovieListCreateViewSet(ListCreateAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()


class MovieRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()


def index(request, page=1):
    movies = models.Movie.objects.all()
    paginator = Paginator(movies, 10)
    movies = paginator.get_page(page)
    return render(request, 'index.html', {'items': movies})
