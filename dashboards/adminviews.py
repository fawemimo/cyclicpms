from django.shortcuts import render

# Create your views here.
from blogs.models import Post
from accounts.models import Profile,User

def director(request):
    # user_id  = User.objects.get()
    profile = Profile.objects.get(user=request.user.id)
    blogs = Post.objects.all().order_by('-date_posted')[:5]
    context = {
    'blogs':blogs,
    'profile':profile
    }
    return render(request,'dashboards/director_template/director.html',context)