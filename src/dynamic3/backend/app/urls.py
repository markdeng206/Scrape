from django.urls import path
from . import views

urlpatterns = [
    path('api/movie/', views.MovieListCreateViewSet.as_view()),
    path('api/movie/<pk>/', views.MovieRetrieveUpdateDestroyViewSet.as_view()),
]
