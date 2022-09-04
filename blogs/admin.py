from django.contrib import admin

# from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    
    list_per_page                   = 25
    list_display                    = ('author','title','date_posted')
    list_display_link               = ('author','title')
    list_filter                     = ('author','date_posted')
admin.site.register(Post,PostAdmin)
