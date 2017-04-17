from django.core.urlresolvers import reverse
from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, blank=True, null=True)
    source = models.FileField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse("media-form", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("media-delete", kwargs={"id": self.id})
