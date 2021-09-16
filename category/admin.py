from django.contrib import admin

# Register your models here.
from .models import  *

admin.site.register(Level)
admin.site.register(Grade)
admin.site.register(Step)
admin.site.register(AddCategoryForEmployee)

