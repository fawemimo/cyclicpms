from django.contrib import admin

# Register your models here.
# from django_summernote.admin import SummernoteModelAdmin

from .models import  *


class ContactAdminArea(admin.AdminSite):
    site_header =   'Contact Admin Point'
    login_template = 'contacts/admin/login.html'

contact_site =  ContactAdminArea(name='ContactAdmin') 


# TEXT = 'This is informations should be based on how to build your circle'
class ContactRequestAdmin(admin.ModelAdmin):
    fieldsets = (
            ('Details', {'fields': ('full_name', 'email')}),

            ('Personal info', {'fields': ('phone',)}),

            ('Information', { 'fields': ('message',),
            }),

            # (('Important dates'), {'fields': ('date_contacted', 'date_review')})
    
    )

    list_display = ('full_name','email','phone','date_contacted','date_review')
    list_display_link = ('full_name','email')
    list_filter = ('date_contacted','date_review')
    list_per_page = 25
    search_fields = ('full_name','email')


# admin.site.register(ContactRequestAdmin)

# @admin.register(ContactRequest,ContactRequestAdmin)

class SummerAdmin(admin.ModelAdmin):
    fieldsets = (
            ('Details', {'fields': ('full_name', 'email')}),

            ('Personal info', {'fields': ('phone',)}),

            ('Information', { 'fields': ('message',),
            }),

            # (('Important dates'), {'fields': ('date_contacted', 'date_review')})
    
    )

    list_display                    = ('full_name','email','phone','date_contacted','date_review')
    list_display_link               = ('full_name','email')
    list_filter                     = ('date_contacted','date_review')
    list_per_page                   = 25
    search_fields                   = ('full_name','email')
    summernote_fields               = '__all__'

admin.site.register(ContactRequest,SummerAdmin)
contact_site.register(ContactRequest,SummerAdmin)



# Email newsletters 

class SubscriberAdminArea(admin.AdminSite):
    site_header = 'Subscriber Admin Point'

subscriber_site = SubscriberAdminArea(name='SubscriberAdmin')


class SubscriberAdmin(admin.ModelAdmin):
    list_display        = ('email','date_subscribed')
    list_per_page       = 25
    list_filter         = ('date_subscribed',)
admin.site.register(Subscriber,SubscriberAdmin) 
subscriber_site.register(Subscriber,SubscriberAdmin)


class MailMessageSummerAdmin(admin.ModelAdmin):
    summernote_fields       = '__all__'
    list_display            = ('title',)
    list_per_page           = 25
    list_filter             = ('date_messaged',)
    search_fields           = ('title',)

    
    
class MailMessageAdminArea(admin.AdminSite):
    site_header = 'Mail Message Admin Point'

mailmessage_site =  MailMessageAdminArea(name='MaiLMessage Admin')   
mailmessage_site.register(MailMessage,MailMessageSummerAdmin)

admin.site.register(MailMessage,MailMessageSummerAdmin)    
