from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission

class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fields = ['name']

admin.site.register(Permission, PermissionAdmin)