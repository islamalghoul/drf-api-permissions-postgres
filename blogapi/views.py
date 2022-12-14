from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import BlogSerializer,PostSerializer
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
# Create your views here.
from .models import Blog,Post


class BlogListView(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class= BlogSerializer
    permission_classes=[IsOwnerOrReadOnly]


class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[IsOwnerOrReadOnly]


class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class= BlogSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]