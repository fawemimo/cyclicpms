from django.contrib import admin

from .models import *

# Register your models here.


class BankDetailAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('user_id','full_name','bank_name','account_number','sort_code',)
    list_display_link = ('user_id','full_name','bank_name')
    list_filter =  ('bank_name',)
    search_fields =  ('user_id','full_name','bank_name')
admin.site.register(BankDetail, BankDetailAdmin)

class PersonalInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['full_name']}),
        ('Date of Birth', {'fields': ['dob','dob_verify']}),
        ('Address', {'fields': ['parmanent_home_address','parmanent_address_verify','contact_address','contact_verify']}),
        ('Contact Number', {'fields': ['phone_number','phone_number_2']}),
        ('Confidentials', {'fields': ['pension_house','pension_number','PAYEE_ID','NHF_ID']})
    ]
    list_per_page = 25
    list_display = ('user_id','full_name','parmanent_home_address','dob_verify','contact_verify','phone_number','pension_house','PAYEE_ID','NHF_ID','employment_date')
    list_editable = ('dob_verify','contact_verify')
    list_display_link = ('user_id','full_name')
    search_fields  = ('user_id','full_name','pension_house','pension_number','PAYEE_ID','NHF_ID')
    list_filter = ('pension_house',)
    date_hierarchy = ('employment_date')
admin.site.register(PersonalInfo,PersonalInfoAdmin)


admin.site.register(Education)

admin.site.register(FileUpload)