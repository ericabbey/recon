from django.conf.urls import url
from django.contrib import admin

from .views import event, event_detail
# from .views import

urlpatterns = [
    url(r'^$', event, name="home"),
    url(r'^(?P<id>\d+)/detail/$', event_detail, name="detail"),
]
