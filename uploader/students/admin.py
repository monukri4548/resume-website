from django.contrib import admin
from .models import Detail

@admin.register(Detail)
class DetailModelAdmin(admin.ModelAdmin):
    list_display=['name','dob','gender','locality','city','pin','state','phone','email','job_type','Profile_picture','my_file']
# Register your models here.