from django.contrib import admin
from . models import Department,Role,Employee

@admin.register(Department)
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','name','location']
    list_display_links = ['id','name']
admin.site.register(Role)
admin.site.register(Employee)