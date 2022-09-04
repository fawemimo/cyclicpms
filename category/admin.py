from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Level)
admin.site.register(Grade)
admin.site.register(Step)
admin.site.register(Leave)
admin.site.register(AddCategory)
admin.site.register(Car)
admin.site.register(Model)
admin.site.register(Order)

