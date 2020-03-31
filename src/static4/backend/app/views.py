from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
import time


def index(request, page=1):
    movies = models.Movie.objects.all()
    paginator = Paginator(movies, 10)
    movies = paginator.get_page(page)
    for movie in movies:
        movie.score_front, movie.score_behind = list(range(int(movie.score / 2))), ((movie.score / 2) % 1) * 100
    movies.total = models.Movie.objects.count()
    time.sleep(5)
    return render(request, 'index.html', {'items': movies})


def detail(request, id):
    movie = models.Movie.objects.get(id=id)
    movie.score_front, movie.score_behind = list(range(int(movie.score / 2))), ((movie.score / 2) % 1) * 100
    time.sleep(5)
    return render(request, 'detail.html', {'item': movie})
