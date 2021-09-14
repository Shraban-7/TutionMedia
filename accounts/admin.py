from django.contrib import admin
from .models import UserProfile,Membership

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Membership)
