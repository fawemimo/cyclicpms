from django.shortcuts import render

def error_page(request):
    return render(request,'error/404.html')

def showFirebaseJS(request):

    data='importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
     'importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"); ' \
     'var firebaseConfig = {' \
     '        apiKey: "AIzaSyAsusPcXCSHm5uZkxvyjqrkzIMp-1lJSDQ",' \
     '        authDomain: "payrollmanagements-b98f9.firebaseapp.com",' \
     '        databaseURL: "https://payrollmanagements-b98f9-default-rtdb.firebaseio.com/",' \
     '        projectId: "payrollmanagements-b98f9",' \
     '        storageBucket: "payrollmanagements-b98f9.appspot.com",' \
     '        messagingSenderId: "payrollmanagements-b98f9.appspot.com",' \
     '        appId: "1:577873096525:web:70556298edfadc85061104",' \
     '        measurementId: "G-LHZB5KKQX8"' \
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
