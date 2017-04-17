from django.contrib import admin
from .models import Post, Comment, like


# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "timestamp"]

    class meta:
        model = Post

class likeAdmin(admin.ModelAdmin):
    list_display = ["blog", "user", "created_at"]


class commentAdmin(admin.ModelAdmin):
    list_display = ["blog", "content", "user", "time"]


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, commentAdmin)
admin.site.register(like, likeAdmin)
