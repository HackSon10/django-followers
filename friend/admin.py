from django.contrib import admin
from .models import Friend
# Register your models here.

class AdminFriend(admin.ModelAdmin):
	list_display = ('user_to','friend_to', 'date')

admin.site.register(Friend, AdminFriend)