import imp
from accounts.models import User
from decouple import config
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def error_page(request):
    return render(request,'error/404.html')

def showFirebaseJS(request):

    data='importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
     'importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"); ' \
     'var firebaseConfig = {' \
     '        apiKey: config(apiKey),' \
     '        authDomain: config(authDomain),' \
     '        databaseURL: config(databaseURL),' \
     '        projectId: config(projectId),' \
     '        storageBucket: config(storageBucket),' \
     '        messagingSenderId: config(messagingSenderId),' \
     '        appId: config(appId),' \
     '        measurementId: config(measurementId)' \
     ' };' \
     'firebase.initializeApp(firebaseConfig);' \
     'const messaging=firebase.messaging();' \
     'messaging.setBackgroundMessageHandler(function (payload) {' \
     '    console.log(payload);' \
     '    const notification=JSON.parse(payload);' \
     '    const notificationOption={' \
     '        body:notification.body,' \
     '        icon:notification.icon' \
     '    };' \
     '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
     '});'

    return HttpResponse(data)



'''
checking for emails and username for both employees and admins
'''
# for checking user email


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get('email')
    user = User.objects.filter(email=email).exists()
    if user:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

# for username


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get('username')
    user = User.objects.filter(username=username).exists()
    if user:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


