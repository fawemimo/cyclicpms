from django.http import HttpResponse
from django.shortcuts import render,redirect
# Email configurations
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login,logout
from accounts.models import User

from accounts.token import account_activation_token

from accounts.forms import HRMRegistrationForm, DirectorProfileForm, UserEditForm
from directors.models import Director
from django.contrib.auth.decorators import login_required



@login_required
def delete_user(request):
    user = User.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return HttpResponse('account deactivate')


@login_required
def dashboard(request):
    return HttpResponse('Dashboard')


def account_register(request): 
    if request.method == 'POST' :     
        hrmform = HRMRegistrationForm(request.POST)
        
        if hrmform.is_valid():
            user = hrmform.save(commit=False)
            
            user.email = hrmform.cleaned_data['email']
            user.set_password(hrmform.cleaned_data['password'])
            user.is_active = False           
            print('successful')
            user.save()


            # Setup Email 
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            # html_message = get_template('contacts/subscribed_text.html').render()
            html_message = render_to_string('accounts/hrm/account_activation_email.html', {
                'user': user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to = user
            send_email = EmailMessage(mail_subject, html_message, to=[to])
            send_email.content_subtype = "html"
            send_email.send()
            return HttpResponse('register successfully and activation send to your email')
        else: 
            print('Failed')    
    else:
       hrmform = HRMRegistrationForm()         

    context = {
        'hrmform':hrmform
    }   

    return render (request, 'accounts/hrm/register.html',context)    

def account_activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None    
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.user_type = 5
        user.save()
        login(request,user)
        return redirect('accounts-complete-profile')
    else:
        return HttpResponse('INVALID TOKEN ACTIVATION')



def complete_profile(request):
    if request.method =='POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()

    else:
        user_form = UserEditForm(instance=request.user)        


    context = {
        'user_form':user_form
    }
    return render(request,'accounts/hrm/complete_profile.html',context)    





""" 


def account_register(request): 
    
    if request.method == 'POST' :     
        hrmform = HRMRegistrationForm(request.POST)
        
        if hrmform.is_valid():
            # user = hrmform.save(commit=False)
            
            # user.email = hrmform.cleaned_data['email']
            # user.set_password(hrmform.cleaned_data['password'])
            # user.is_active = False
            # print('successful')
            # user.save()
            
            first_name=hrmform.cleaned_data["first_name"]
            last_name=hrmform.cleaned_data["last_name"]
            username=hrmform.cleaned_data["username"]
            email=hrmform.cleaned_data["email"]
            password=hrmform.cleaned_data["password"]
            password2=hrmform.cleaned_data["password2"]
            company_name=hrmform.cleaned_data["company_name"]
            phone_number=hrmform.cleaned_data["phone_number"]

            # try:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,phone_number=phone_number,user_type=5,is_active=False)

            directors = Director.objects.get(user=user)
            user.directors.company = company_name
            user.save()
            print('form valid')
            # except:
            #     print('oh it seems bad')   

            # Setup Email 
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            # html_message = get_template('contacts/subscribed_text.html').render()
            html_message = render_to_string('accounts/hrm/account_activation_email.html', {
                'user': email,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to = user
            send_email = EmailMessage(mail_subject, html_message, to=[to])
            send_email.content_subtype = "html"
            send_email.send()

    else:   
        print('form invalid')
        # hrmform = HRMRegistrationForm()
        # return HttpResponse('Method is not allowed')

    context  = {
        'hrmform':hrmform,
        
    }
    return render (request, 'accounts/hrm/register.html',context)         

 """

