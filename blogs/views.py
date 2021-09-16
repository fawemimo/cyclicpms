from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

from .forms import PostForm
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, 
    UpdateView,
    DeleteView
)
from django.views.generic import View, TemplateView
from django.http import JsonResponse, request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from accounts.models import *
import requests
from django.core.files.storage import FileSystemStorage

def blog(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render (request,'blog/index.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/post_form.html'
    success_url = reverse_lazy('bloghome')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def post_create_view(request):
    if request.method != 'POST':
        return redirect('')
    else:
        title           = request.POST['title']
        content         = request.POST['content']
        video           = request.POST['video']
        image           = request.POST['image']
        thumbnail       = request.POST['thumbnail']
        
        posts = Post(title=title,content=content,video=video,image=image,thumbnail=thumbnail)
        
        posts.save()

@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Blog added successfully')
            print('Blog added successfull')
            return redirect('user-posts')
        else:
            messages.error(request,'Blog added failed')
            print('failed')
            return redirect('post_create_view')
    else:
        form = PostForm()
    context = {
        'form':form
    }    
    return render(request,'blogs/post_form.html',context)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post    
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author.id = self.request.user.id
        return super().form_valid(form)    
    

    def test_func(self):
        post = self.get_object()
        if self.request.user.id == post.author.id:
            return True
            
        return False    
    
    
@login_required
def post_update(request,pk):
    
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':
        
        form    = PostForm(request.POST,request.FILES,instance=posts)
        # title   = form.cleaned_data'title')
        if form.is_valid():
            form.save()
            messages.success(request, ' updated successfully')
            return redirect('post-detail' ,pk=posts.id)
        else:
            messages.error(request, ' failed to update')
            return redirect('post-detail' ,pk=posts.id)
    else:
        form = PostForm(instance=posts)
    context = {
        'form':form,
        'posts':posts,
    }    
    
    return render(request,'blogs/posts_update.html',context)    


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url =  reverse_lazy('bloghome')


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True        
        return False  
    
    
# @login_required
# def post_edit(request, pk):
#     post = PostModel.objects.get(id=pk)
#     if request.method == 'POST':
#         form = PostUpdateForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('blog-post-detail', pk=post.id)
#     else:
#         form = PostUpdateForm(instance=post)
#     context = {
#         'post': post,
#         'form': form,
#     }
#     return render(request, 'blog/post_edit.html', context)


# @login_required
# def post_delete(request, pk):
#     post = PostModel.objects.get(id=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog-index')
#     context = {
#         'post': post
#     }
#     return render(request, 'blog/post_delete.html', context)    