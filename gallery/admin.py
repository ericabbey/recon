from django.contrib import admin
from .models import Media

class GalAdmin(admin.ModelAdmin):
    list_display=["title", "artist","type", "source", "timestamp"]
admin.site.register(Media, GalAdmin)
