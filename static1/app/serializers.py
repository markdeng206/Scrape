from rest_framework.serializers import ModelSerializer
from .models import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'alias', 'cover', 'rank', 'regions',
                  'categories', 'score', 'minute', 'directors',
                  'drama', 'actors', 'photos', 'published_at']
