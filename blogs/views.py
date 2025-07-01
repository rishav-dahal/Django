from django.shortcuts import render
from rest_framework import generics
from . models import Blog , Comment
from .serializers import BlogSerializer ,CommentSerializer
from .pagination import CustomPagination
from rest_framework.filters import SearchFilter , OrderingFilter
# Create your views here.

class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title','blog_body'] # specify which field you want to search if we use ^blog_title then when search it search with sentencence starting from searching word 
    Ordering_fields=['id']
    
class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
