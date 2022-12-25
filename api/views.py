from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from api.permissions import PostUserWritePermission
from blogs.models import *
from .serializers import *
from rest_framework.permissions import (
    DjangoModelPermissions,
    SAFE_METHODS,
    BasePermission,
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly,
    AllowAny,
)
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions,filters
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer








"""
USING VIEW SETS
"""
class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()

    # overriding the default  queryset   \
    # def get_object(self,queryset=None, **kwargs):
    #     item =self.kwargs.get('pk')
    #     return get_object_or_404(Post, slug=item)

    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.postobjects.filter(author=user)    

# class PostList(viewsets.ViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(data=request.data)
#         return Response(serializer_class.data)


class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=str.HTTP_400_BAD_REQUEST)


class CustomUserAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)

        if reg_serializer.is_valid():
            newuser = reg_serializer.save()

            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

class PostList(generics.ListCreateAPIView):
    # permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(author=user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    # queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        # slug= self.kwargs['pk']
        # print(slug)
        # return Post.objects.filter(id=slug)
        slug = self.request.query_params.get('slug', None)
        return Post.postobjects.filter(slug=slug)


    def get_object(self):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
