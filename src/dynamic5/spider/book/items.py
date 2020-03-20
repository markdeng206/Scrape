# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from app.models import Book, Tag, Publisher, Person, Comment

class BookItem(DjangoItem):
    django_model = Book

class TagItem(DjangoItem):
    django_model = Tag

class PublisherItem(DjangoItem):
    django_model = Publisher

class CommentItem(DjangoItem):
    django_model = Comment

class PersonItem(DjangoItem):
    django_model = Person
