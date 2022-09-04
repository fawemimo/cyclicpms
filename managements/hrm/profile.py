from urllib import request
from django.http import HttpResponse, JsonResponse
from directors.models import Director
from accounts.models import User
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages

'''
Director profile updating

'''
# director editing profile
def director_profile(request,name='Default name'):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        director = Director.objects.get(user=request.user.id)
        print('oh HRM')
        context = {
            'director': director
        }
        return render(request, 'managements/director_template/director_profile.html', context)


def director_profile_save(request):
    if request.method != 'POST':
        return redirect('director_profile')
    else:

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        other_name = request.POST.get('other_name')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        try:
            user = User.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.other_name = other_name
            director = Director.objects.get(user=request.user.id)
            director.profile_pic = profile_pic
            if password != None and password != "":
                user.set_password(password)

            user.save()
            messages.success(request, 'Profile change successfully')
            return redirect('director_profile')
        except:
            messages.error(request, 'Failed to make changes')
            return redirect('director_profile')


'''
END Director profile updating

'''