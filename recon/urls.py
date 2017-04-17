"""recon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from blogs.views import post_update, admin_post, post_delete, post_create
from base.views import index, about
from account.views import post, message
from event.views import  event_update ,admin_events , event_delete, event_create
from gallery.views import media_update, admin_media ,media_delete, media_create

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include("blogs.urls", namespace="blog")),
    url(r'^gallery/', include("gallery.urls", namespace="gallery")),
    url(r'^events/', include("event.urls", namespace="events")),
    url(r'^$', index, name="home" ),
    url(r'^about/$', about, name="about"),
    url(r'^post/$', post, name="post" ),
    url(r'^message/$', message, name="message" ),

    url(r'^super/', include("account.urls", namespace="super")),
# post urls
    url(r'^super/blog/delete/(?P<id>\d+)/$', post_delete, name="blog-delete"),
    url(r'^super/blog/create', post_create, name="blog-create"),
    url(r'^super/blog/edit/(?P<id>\d+)/$', post_update,  name="blog-form"),
    url(r'^super/blog', admin_post, name="admin-blog"),
 # events urls
    url(r'^super/events/delete/(?P<id>\d+)/$', event_delete, name="event-delete"),
    url(r'^super/events/create', event_create, name="event-create"),
    url(r'^super/events/edit/(?P<id>\d+)/$', event_update,  name="event-form"),
    url(r'^super/events', admin_events, name="admin-event"),
# gallery urls
    url(r'^super/media/delete/(?P<id>\d+)/$', media_delete, name="media-delete"),
    url(r'^super/media/create', media_create, name="media-create"),
    url(r'^super/media/edit/(?P<id>\d+)/$', media_update,  name="media-form"),
    url(r'^super/media', admin_media, name="admin-media")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
