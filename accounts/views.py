from accounts.models import Profile
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

# Create your views here.
from managements.models import *
from managements.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView,FormView
from .forms import LoginForm,UserConfirmForm,OtpCodeForm, ProfileUpdateForm
from django.core.files.storage import FileSystemStorage
# Notifications django in-built alerts 

from django.contrib import messages, auth

# Verification of Email

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def login_page(request):
    form            = LoginForm(request.POST or None)
    confirm         = UserConfirmForm(request.POST or None)
    context = {
        'form':form,
        'confirm':confirm
    }
    next_           = request.GET.get('next')
    next_post       = request.POST.get('next')
    redirect_path   = next_ or next_post or None
    if form.is_valid():
        email           = form.cleaned_data.get('email')
        password        = form.cleaned_data.get('password')
        user            = authenticate(request, username=email,password=password)
        if user is not None:
            request.session['pk'] = user.pk   

            login(request,user)       
            
        
            return redirect('accounts-verify') 
            try:
                del request.session['email']
            except:
                pass
            if is_safe_url(redirect_path,request.get_host()):
                
                return redirect(redirect_path)
            else:
                messages.success(request,'Enter OTP code sent to your phone')
                return redirect('accounts-verify')  
        else:
            messages.error(request,'Input OTP code sent to your phone')
            return redirect(redirect_path)
    return render(request,'accounts/login.html',context)    


    
    
# Authentication and verification of users through OTPCODES 

from accounts.utils import send_sms
    
@login_required
def verify_view(request):
    form        = OtpCodeForm(request.POST or None)
    
    pk          = request.session.get('pk')

    if pk:

        user        = User.objects.get(pk=pk)
        otpcode     = user.otpcode
        otp_user    = f'{user.email}: {user.otpcode}'

        if not request.POST:
            # sending sms
            # 
            # print(otp_user)
            send_sms(otp_user,user.phone_number) 
            
        if form.is_valid():
            
            num             = form.cleaned_data.get('otp')
            
            if str(otpcode) == num: 
              
                otpcode.save()
                
                login(request, user)
                if request.user.user_type == 1 :
                    
                    # form validations for dashboard 
                    messages.success(request,'You have successfully login')
                    return redirect ('home')
                # elif request.user.user_type == 'is_admin' :
                #     # form validations for dashboard 
                #     return redirect ('bloghome')
                # elif request.user.user_type == 'is_auditor' :
                #     # form validations for dashboard 
                #     return redirect ('accounts-profile')
                # elif request.user.user_type == 'is_accountant' :
                #     # form validations for dashboard 
                #     return redirect ('home')
                elif request.user.user_type == 5 :
                    # form validations for dashboard 
                    messages.success(request,'You have successfully login')
                    return redirect ('directors')
                else:
                    messages.error(request,'Invalid login crendentials')
            
                
            else:
                messages.error(request,'Provide a valid OTP code')
                return redirect('accounts-login')

    context = {
        'form':form,

    }                

    return render(request,'accounts/verify_login.html',context)  


# Logout views 

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('home')      


# for users to update their profile pics

def profile(request):
    profile = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form      = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid():
            image       = request.FILES['image']
            fs          = FileSystemStorage()
            filename    = fs.save(image.name,image)
            image_url   = fs.url(filename)
            form.save()
            # user dashboard
            return redirect('')

    else:
        form      = ProfileUpdateForm(instance=request.user.profile)

    context = {

        'form':form,
        'profile':profile

    }
    return render(request,'accounts/profile.html',context)



def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            session_year_id=form.cleaned_data["session_year_id"]
            course_id=form.cleaned_data["course"]
            sex=form.cleaned_data["sex"]

            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.students.address=address
                course_obj=Courses.objects.get(id=course_id)
                user.students.course_id=course_obj
                session_year=SessionYearModel.object.get(id=session_year_id)
                user.students.session_year_id=session_year
                user.students.gender=sex
                user.students.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Student")
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request,"Failed to Add Student")
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form = AddStudentForm(request.POST)
            return render(request, "hod_template/add_student_template.html", {"form": form})