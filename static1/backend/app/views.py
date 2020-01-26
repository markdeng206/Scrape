from django.shortcuts import render
from . import models
from django.core.paginator import Paginator


def index(request, page=1):
    movies = models.Movie.objects.all()
    paginator = Paginator(movies, 10)
    movies = paginator.get_page(page)
    return render(request, 'index.html', {'items': movies})


def detail(request, id):
    movie = models.Movie.objects.get(id=id)
    return render(request, 'detail.html', {'item': movie})
