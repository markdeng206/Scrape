# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import django
from scrapy_djangoitem import DjangoItem
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'static1.core.settings')
django.setup()

from app.models import Movie


class MovieItem(DjangoItem):
    django_model = Movie
