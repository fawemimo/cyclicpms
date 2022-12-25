
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from accounts import views

# from contacts.admin import *
# from accounts.admin import profile_site,otpcodes_site
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)


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
    path('requisitions/',include('requisitions.urls')),
    path('set_salary/',include('set_salary.urls')),
    path('payroll/',include('payroll.urls')),

    # API 's
    path('api/',include('api.urls')),
    path('api/accounts/',include('accounts.api_urls')),
    path('api-auth/',include('rest_framework.urls'), name='rest_framework'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    # path('todo/',include('todo.urls')),
    # path('api/auth/tokens/',include('rest_auth.urls')),
    # path to django packages 
    # path('summernote/',include('django_summernote.urls')),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 



admin.site.index_title = 'Management System'
