from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from . import models
from . import serializers
import base64
from core.settings import SECRET_KEY


class MovieListCreateViewSet(ListCreateAPIView):
    serializer_class = serializers.MovieIndexSerializer
    queryset = models.Movie.objects.all()


class MovieRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieDetailSerializer
    queryset = models.Movie.objects.all()
    
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        # Decode key to id
        key = self.kwargs[lookup_url_kwarg]
        id = base64.b64decode(key).decode('utf-8').replace(SECRET_KEY, '')
        obj = get_object_or_404(queryset, **{'id': int(id)})
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj
