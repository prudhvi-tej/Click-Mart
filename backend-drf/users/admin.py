from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class Useradmin(UserAdmin):
    list_display=['email','first_name','last_name','is_active']
    fieldsets=()


admin.site.register(User,Useradmin)