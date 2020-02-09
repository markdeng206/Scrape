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

