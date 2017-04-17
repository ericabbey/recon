from django.db import models
from django.core.urlresolvers import reverse


class Event(models.Model):
    title = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100, null=True, blank=True,)
    venue = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=False, auto_now=False)
    cover = models.FileField()
    map_image = models.FileField()
    map_url = models.URLField(null=True, blank=True,)

    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("event-form", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("event-delete", kwargs={"id": self.id})
