from rest_framework.serializers import ModelSerializer, RelatedField, ReadOnlyField
from .models import Book, Comment

class CommentIndexSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']

class BookIndexSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'authors', 'cover', 'score']

class CommentDetailSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BookDetailSerializer(ModelSerializer):
    comments = CommentIndexSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'
