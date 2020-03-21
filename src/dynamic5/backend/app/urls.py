from django.urls import path
from . import views

urlpatterns = [
    path('api/book/', views.BookListCreateViewSet.as_view()),
    path('api/book/<pk>/', views.BookRetrieveUpdateDestroyViewSet.as_view()),
    path('api/comment/', views.CommentListCreateViewSet.as_view()),
    path('api/comment/<pk>/', views.CommentRetrieveUpdateDestroyViewSet.as_view()),
]
