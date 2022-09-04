"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


# from accounts import views



# from contacts.admin import *
# from accounts.admin import profile_site,otpcodes_site


urlpatterns = [
    path('admin/', admin.site.urls),
    # path to some models 
    # path('contactadmin/',contact_site.urls),
    # path('profileadmin/',profile_site.urls),
    # path('otpcodesadmin/',otpcodes_site.urls),
    # path('subscribersadmin/',subscriber_site.urls),
    # path('mailmessageadmin/',mailmessage_site.urls),
    

    # install apps urls 
    
    path('',include('payroll.urls')),
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),
    path('confidentials/',include('confidentials.urls')),
    path('blogs/',include('blogs.urls')),
    path('managements/',include('managements.urls')),
    path('dashboards/',include('dashboards.urls')),
    path('leave/',include('leave.urls')),
    path('category/',include('category.urls')),

    # path to django packages 
    # path('summernote/',include('django_summernote.urls')),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 



admin.site.index_title = 'Management System'
