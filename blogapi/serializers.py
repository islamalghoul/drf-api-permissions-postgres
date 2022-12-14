from rest_framework import serializers

from .models import Blog,Post
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Blog
        # fields=['id','name', 'owner', 'description']
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        # fields=['id','name', 'owner', 'description']
        fields='__all__'