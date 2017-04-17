import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from account.models import UserProfile
from .forms import MediaForm
from .models import Media

img = ('jpg', 'jpeg', 'bmp', 'png', )
vid = ('flv', 'mp4', 'mkv')
aud = ('mp3', 'aud', 'ogg')

def pics(request):
    media = Media.objects.filter(type="Image")
    return render (request, 'gallery.html',  {"media": media})

def vids(request):
    media = Media.objects.filter(type="Video")
    return render (request, 'gal-vid.html', {"media": media})

def auds(request):
    media = Media.objects.filter(type="Audio")
    return render (request, 'gal-aud.html', {"media": media})


@login_required(login_url='login')
def media_create(request):
    instance = ""
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.title == "editor":
        form = MediaForm(request.POST or None, request.FILES or None)
        print (form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            name, extention = os.path.splitext(instance.source.url)
            ext = extention.replace(".", "", 1)
            if ext in img:
                instance.type = "Image"
            elif ext in aud:
                instance.type = "Audio"
            elif ext in vid:
                instance.type = "Video"

            instance.save()
            created = instance
            print(created)
            if created:
                messages.success(request, "The media \""+str(instance.title)+"\" is succefully updated")
            else:
                messages.info(request, "Oops an error occured")
            return HttpResponseRedirect(reverse("admin-media"))
        context = {
             "form": form,
             "instance": instance
        }
    else:
        messages.info(request, "you are not authorized to do that")
        return redirect(reverse("home"))
    return render (request, 'super/media-form.html', context)


@login_required(login_url='login')
def media_update(request, id=None):
    instance = get_object_or_404(Media, id=id)
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.title == "editor":
        form = MediaForm(request.POST or None, request.FILES or None, instance=instance)
        print (form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            name, extention = os.path.splitext(instance.source.url)
            ext = extention.replace(".", "", 1)
            if ext in img:
                instance.type = "Image"
            elif ext in aud:
                instance.type = "Audio"
            elif ext in vid:
                instance.type = "Video"

            instance.save()
            created = instance
            print(created)
            if created:
                messages.success(request, "The media \""+str(instance.title)+"\" is succefully updated")
            else:
                messages.info(request, "Oops an error occured")
            return HttpResponseRedirect(reverse("admin-media"))
        context = {
             "form": form,
             "instance": instance
        }
    else:
        messages.info(request, "you are not authorized to do that")
        return redirect(reverse("home"))
    return render (request, 'super/media-form.html', context )


@login_required(login_url='login')
def media_delete(request, id=None):
    instance = get_object_or_404(Media, id=id)
    instance.delete()
    return redirect(reverse("admin-media"))


@login_required(login_url='login')
def admin_media(request):
    media = Media.objects.all().order_by("-timestamp", "-updated")
    return render (request, 'super/all-media.html', {"media": media})
