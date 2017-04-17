from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_create,
    post_detail,
    post_list,
    post_delete,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
]
