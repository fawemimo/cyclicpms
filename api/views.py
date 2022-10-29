from rest_framework import generics
from blogs.models import *
from .serializers import *

class PostList(generics.ListCreateAPIView):
    queryset =Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):    
    queryset =Post.postobjects.all()
    serializer_class = PostSerializer