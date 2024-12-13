from django.contrib import admin
from .models import User, JobRole


# from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'email', 'user_name', 'phone_number', 'job_role', 'company', 'is_active', 'is_staff', 'created', 'updated')
    list_filter = ('user_name', 'is_active', 'is_staff', 'job_role')
    ordering = ('id',)


admin.site.register(User, UserAdmin)
admin.site.register(JobRole)
