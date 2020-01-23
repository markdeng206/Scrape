from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page>', views.index, name='index'),
    path('api/movie/', views.MovieListCreateViewSet.as_view()),
    path('api/movie/<pk>/', views.MovieRetrieveUpdateDestroyViewSet.as_view()),
]
