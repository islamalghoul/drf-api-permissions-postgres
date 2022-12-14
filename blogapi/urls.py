from django.urls import path
from .views import BlogListView,BlogDetailView,PostListView,PostDetailView
urlpatterns = [
   path('', BlogListView.as_view(), name='blog_list'),
   path('<int:pk>', BlogDetailView.as_view(),name='blog_detail'),
   path('post', PostListView.as_view(), name='post_list'),
   path('post/<int:pk>', PostDetailView.as_view(),name='post_detail')
]