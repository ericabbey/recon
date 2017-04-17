from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True,)
    content = models.TextField()
    # height = models.IntegerField(default=0)
    # width = models.IntegerField(default=0)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    num_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("blog-form", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("blog-delete", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp"]


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default='')
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, default='', blank=True, null=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return self.blog.title

class like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default='')
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title
