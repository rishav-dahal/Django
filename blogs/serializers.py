from . models import Blog , Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)     # here variable i.e (comments) should be related name written in comment model
    class Meta:
        model = Blog
        fields = '__all__'