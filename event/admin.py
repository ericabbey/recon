from django.contrib import admin
from .models import Event

class eventAdmin(admin.ModelAdmin):
        list_display = ["title", "organizer", "theme", "date"]
        list_filter = ('date',)
        search_fields = ('title',)
        ordering = ('date',)

admin.site.register(Event, eventAdmin)
