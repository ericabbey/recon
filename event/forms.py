from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "organizer",
            "venue",
            "theme",
            "date",
            "cover",
            "map_image",
            "map_url"
        ]
