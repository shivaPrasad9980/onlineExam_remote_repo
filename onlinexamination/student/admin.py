from django.contrib import admin
from . models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','Firstname','Lastname','Contact','Address','Username','Password','ProfilePicture']

admin.site.register(Student,StudentAdmin)