from django.conf.urls import url

from .views import pics, vids, auds

urlpatterns = [
        url(r'^pictures/', pics, name="pictures"),
        url(r'^$', pics, name="home"),
        url(r'^videos/$', vids, name="videos"),
        url(r'^audio/$', auds, name="audio"),
]
