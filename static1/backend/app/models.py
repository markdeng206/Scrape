from django.contrib.postgres.fields import ArrayField, JSONField
from django.db.models import CharField, Model, FloatField, IntegerField, DateField, DateTimeField, TextField, AutoField


class Movie(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True)
    alias = CharField(max_length=255, null=True, blank=True)
    cover = CharField(max_length=255, null=True, blank=True)
    categories = ArrayField(CharField(max_length=255, null=True, blank=True), null=True, blank=True)
    regions = ArrayField(CharField(max_length=255, null=True, blank=True), null=True, blank=True)
    actors = JSONField(null=True, blank=True)
    directors = JSONField(null=True, blank=True)
    score = FloatField(null=True, blank=True)
    rank = IntegerField(null=True, blank=True)
    minute = IntegerField(null=True, blank=True)
    drama = TextField(null=True, blank=True)
    photos = ArrayField(CharField(max_length=500, null=True, blank=True), null=True, blank=True)
    published_at = DateField(null=True, blank=True)
    updated_at = DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = 'app'
