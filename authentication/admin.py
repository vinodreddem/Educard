from django.contrib import admin

from EduSphere.models import *
from EduSphere.models import Master

# Register your models here.
from django.contrib.auth.models import Permission

class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fields = ['name']

admin.site.register(Permission, PermissionAdmin)
admin.site.register(Address)
admin.site.register(Class)
admin.site.register(Master.MstSubject)
admin.site.register(Master.MstClass)
admin.site.register(School)
admin.site.register(SchoolTeacherClassSubject)
admin.site.register(Subject)
admin.site.register(Teacher)