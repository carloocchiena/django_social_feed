from django.contrib import admin
from django.contrib.auth.models import User

from . import models

# This is to handle all user data within a single admin section
class ProfileInline(admin.StackedInline):
    model = models.Profile
    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Post)
