from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, OtpCode,Profile
from django.utils.html import format_html

# custom filter 
from django.contrib.admin import SimpleListFilter

class EmailFilter(admin.SimpleListFilter):
    title = 'Email Filter'
    parameter_name = 'user_email'

    def lookups(self, request, model_admin):
        return (
            ('has_email','has_email'),
            ('no_email','no_email')
        )
    def queryset(self,request,queryset):
        if not self.value():
            return queryset

            # has no email 
        if self.value().lower() == 'has_email'    :
            return queryset.exclude(user__email='')

        if self.value().lower() == 'no_email':
            return queryset.filter(user__email='')

# Register your models here.
class UserAdmin(UserAdmin):
    list_display =('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    search_fields = ('first_name','email')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_per_page = 25
    list_filter = (EmailFilter,'date_joined','last_login','is_active')
    fieldsets = ()
    
admin.site.register(User,UserAdmin)    


class OtpCodeAdminArea(admin.AdminSite):
    site_header = 'OTPcodes Admin Point'

otpcodes_site = OtpCodeAdminArea(name='OtpcodesAdmin')
admin.site.register(OtpCode)



class ProfileAdminArea(admin.AdminSite):
    site_header = 'Profile Admin Point'

profile_site = ProfileAdminArea(name='ProfileAdmin')    
profile_site.register(Profile)

TEXT = 'User data are neccessary for handling different login'


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
            ('User Data', {'fields': ('user',),
            'description': '%s' % TEXT}),

            

            ('Information', { 'fields': ('image',)}),

            (('Important dates'), {'fields': ( 'date_updated',)})
    
    )

    list_display = ('full_name','user','date_updated')
    list_display_link = ('full_name','user')
    list_filter = ('date_updated',EmailFilter)
    list_per_page = 25
    search_fields = ('user',)
admin.site.register(Profile,ProfileAdmin)