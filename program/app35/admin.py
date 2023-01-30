from django.contrib import admin

# Register your models here.

from app35.models import login,stud_Reg,Question

admin.site.register(login)
admin.site.register(stud_Reg)
admin.site.register(Question)