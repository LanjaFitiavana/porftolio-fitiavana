from django.contrib import admin
from .models import MessageEmail
from django.contrib.auth.admin import UserAdmin


class MessageAdmin(UserAdmin):
    list_display = ['nom','email','contenu','date_sms']
    list_filter =['-date_sms']

admin.site.register(MessageEmail)
