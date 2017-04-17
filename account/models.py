from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_img = models.FileField(blank=True)
    title = models.CharField(max_length=10)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'profile for %s' % self.user.username


class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj')
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)


class Chat(models.Model):
    sender = models.ForeignKey(User, related_name="sender", )
    receiver = models.ForeignKey(User, related_name="receiver")
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.message

    def sent(self, s, r):
        return self.objects.get(sender=s, receiver=r)
