from django.shortcuts import render,redirect
from .forms import ContactRequestForm, SubscribersForm,MailMessagesForm
from django.contrib import messages
from .models import Subscriber, ContactRequest
from django.http import JsonResponse

# Email configurations 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
import requests
from django.template import Context
from django.template.loader import get_template
from django.conf import settings




def contact(request):
    if request.method == 'POST':        
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your request has been posted')
            
            return redirect('home')     
        else:
            messages.error(request,'Your rquest is not posted')
            return redirect('contacts')        
    else:
        form =   ContactRequestForm()
    context = {
        'form':form,
    }
    return render(request,'contacts/contacts.html',context)


def getContact(request):
    contact = ContactRequest.objects.all()
    return JsonResponse({'contact':list(contact.values())})

# email subscribers 

def subscribers(request):
    if request.method == 'POST':

        form = SubscribersForm(request.POST)        
        if form.is_valid():
            instance = form.save(commit=False)
            email = form.cleaned_data.get('email')
            if Subscriber.objects.filter(email = instance.email).exists():
                messages.warning(request,'You already subscribe')
                return redirect('contacts-letter')
            else:
                instance.save()
                messages.success(request, 'Subcriptions successful')
                
                # send email 
                current_site = get_current_site(request)
                mail_subject = 'You have now subscribe to our Newsletter'
                html_message = get_template('contacts/subscribed_text.html').render()   
                email = form.cleaned_data.get('email')
                to = email
                send_email = EmailMessage(mail_subject,html_message,to=[to])
                send_email.content_subtype = "html"
                send_email.send()
                messages.success(request,'Mail sent successfully')
                return redirect('home')

    else:
        form = SubscribersForm()
        
    context = {
            'form':form
    }
    return render(request,'contacts/subscribers.html',context)


def unsubscribe(request):

    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if Subscriber.objects.filter(email=instance.email).exists():
                Subscriber.objects.filter(email=instance.email).delete()
                messages.success(request,'You have successfully unsubscribe')
                
                return redirect('contacts-letter')
            else:
                messages.warning(request,'You are not a subscriber ')
                
                return redirect('contacts-unsubcribe')
    else:
        form =   SubscribersForm()  
        # return redirect('contacts-letter')  
    context = {
        'form':form
    } 
    return render(request,'contacts/unsubscribe.html',context)



# sending messages to all emails subscribers 

def mail_letter(request):
    if request.method == 'POST':
        email = ''

        subscribe = SubscribersForm(request.POST)
        form = MailMessagesForm(request.POST)
        if form.is_valid():
            email = Subscriber.objects.filter(email=email)
            form.save()
        
            
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')           
            messages.success(request,'message sent successfully')
            
            # send email 
            current_site = get_current_site(request)
            mail_subject = title
            html_message = render_to_string('contacts/mails.html',{
                'title': title,
                'domain' : current_site,
                'message':message
            }
            )
            email = form.cleaned_data.get('email')
            
            to = email
            send_email = EmailMessage(mail_subject,html_message,to=[to])
            send_email.send()
            messages.success(request,'Mail sent successfully')
                
            
            return redirect('home')
        else:
            messages.error(request,'message failed')
            return redirect('contacts-mail')
    else:
        form = MailMessagesForm()      
    
    context = {
        'form':form
    }
    return render(request,'contacts/mail_letter.html',context)