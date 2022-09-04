import requests
from django import views
from django.contrib import messages
from django.contrib.messages.api import success
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import User
from confidentials.models import *
from managements.models import *

# Create your views here.
from .forms import *


# returning success page after form filling 
def success_page(request):
    return render(request,'confidentials/success_page.html')

# using js to upload multiple file 

def file_upload(request):
    return render (request,'confidentials/file_upload.html')

# saving the file uploaded 
@csrf_exempt
def file_upload_save(request):
   
    user_id     = request.POST.get('user_id')
    # django file storages       
    fs          = FileSystemStorage()
    file1       = request.FILES.get('file1')
    file1_path  = fs.save(file1.name,file1)    
    file2       = request.FILES.get('file2')
    file2_path  = fs.save(file2.name,file2)    
    file3       = request.FILES.get('file3')
    file3_path  = fs.save(file3.name,file3)
    
    # if users has file in the table before 
    has_file    = FileUpload.objects.all().filter(user_id=user_id)
    if has_file:
        # send error messages to user that already submit file  
        messages.error(request,'You already have file submitted')
        return redirect('file_upload')
    
    # saving the files in the table 
    file_uploads    = FileUpload(user_id=user_id,file1=file1_path,file2=file2_path,file3=file3_path)
    
    file_uploads.save()
    # sending messages on success 
    messages.success(request,'File uploaded successfully')
    
    # sending email for confirmation 
    
    return redirect('success_page')


# views for personal info 
def personalinfo(request):
    if request.method == 'POST':
        user_id                              = request.POST['user_id']
        full_name                            = request.POST.get('full_name')
        dob                                  = request.POST['dob']
        dob_verify                           = request.POST.get('dob_verify')
        parmanent_home_address               = request.POST['parmanent_home_address']
        parmanent_address_verify             = request.POST.get('parmanent_address_verify')
        contact_address                      = request.POST['contact_address']
        contact_verify                       = request.POST.get('contact_verify')
        phone_number                         = request.POST.get('phone_number')
        phone_number_2                       = request.POST['phone_number_2']
        pension_house                        = request.POST['pension_house']
        pension_number                       = request.POST['pension_number']
        PAYEE_ID                             = request.POST['PAYEE_ID']
        NHF_ID                               = request.POST['NHF_ID']
        employment_date                      = request.POST.get('employment_date')
        
        # verify if personal info have already saved 
        
        has_personalinfo = PersonalInfo.objects.all().filter(user_id=user_id)
        if has_personalinfo:
            messages.error(request, 'You already have personal info saved')
            # print('Already have info')
            return redirect('personalinfo')
        
        # save the personal info into the table 
        
        personal  = PersonalInfo(NHF_ID=NHF_ID,pension_number=pension_number,user_id=user_id,full_name=full_name,dob=dob,dob_verify=0,parmanent_home_address=parmanent_home_address,parmanent_address_verify=0,contact_address=contact_address,contact_verify=0,phone_number=phone_number,phone_number_2=phone_number_2,pension_house=pension_house,PAYEE_ID=PAYEE_ID,employment_date=employment_date)
        personal.save()
        messages.success(request, 'Personal info received and saved')
        # print('success')
        return redirect('bankdetail')        
     
    else:
       messages.error(request,'Failed to save personal info')
    #    return redirect('personalinfo')
    return render(request,'confidentials/personalinfo.html')

# views for bank details 

def bankdetail(request):
    if request.method == 'POST':
        
        form            = BankDetailForm(request.POST)
        if form.is_valid():
            
            # grab the user ID for verification 
            
            user_id         = form.cleaned_data.get('user_id')
            if request.user.is_authenticated:
                user_id = request.user.id
                
                # if it has bank detials 
                
                has_bankdetails = BankDetail.objects.all().filter(user_id=user_id)
                if has_bankdetails:
                    messages.error(request, 'You already have bank info saved')
                    print('Already have info')
                    return redirect('bankdetail')
                
            # save the form into the table 
            form.save()    
            print('success')
            messages.success(request,'Bank details received and saved')
            return redirect('education')
        else:
            print('failed')   
            messages.error(request,'Bank details failed to save') 
            return redirect('bankdetail')
    else:
        form        = BankDetailForm()        
        
    
    context = {
    'form':form
    }

    return render(request,'confidentials/bank.html',context)

# views for education 

def education(request):
    if request.method == 'POST':
        form            = EducationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            # grab the user id  
            
            user_id         = form.cleaned_data.get('user_id')
            if request.user.is_authenticated:
                user_id = request.user.id
                # if it has form 
                has_education = Education.objects.all().filter(user_id=user_id)
                if has_education:
                    
                    # print error ang go to the same page 
                     
                    messages.error(request, 'You already have education info saved')
                    print('Already have info')
                    return redirect('education')
                
            #  on success submission go to form all save awaiting verification 
                   
            print('success')
            messages.success(request,'Education details received and saved')
            return redirect('personalinfo')
        else:
            print('failed')   
            messages.error(request,'Education details failed to save') 
            return redirect('education')
    else:
        form        = EducationForm()        
        
    
    context = {
    'form':form
    }

    return render(request,'confidentials/eduction.html',context)
