from rest_framework.serializers import ModelSerializer
from .models import Movie


class MovieIndexSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'alias', 'cover', 'categories', 'published_at', 'minute', 'score', 'regions']


class MovieDetailSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
