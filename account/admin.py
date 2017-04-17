from django.contrib import admin
from .models import UserProfile, Action, Chat

class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('message', 'sender', 'receiver', 'created')
    list_filter = ('created',)
    search_fields = ('receiver',)

admin.site.register(Action, ActionAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(UserProfile)
