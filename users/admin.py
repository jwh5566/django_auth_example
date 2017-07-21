from django.contrib import admin
from .models import User


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email', 'nickname']

admin.site.register(User, RegisterAdmin)