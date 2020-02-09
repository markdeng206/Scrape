from django.urls import path
from . import views

urlpatterns = [
    path('api/news/', views.NewsListCreateViewSet.as_view()),
    path('api/news/<pk>/', views.NewsRetrieveUpdateDestroyViewSet.as_view()),
]
