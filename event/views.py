from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import EventForm
from .models import Event
from account.models import UserProfile
from account.utils import create_action

def event(request):
    event = Event.objects.all()
    return render (request, 'events.html', {'events': event })


def event_detail(request , id=None):
    instance = get_object_or_404(Event, id=id)
    context = {
    "instance": instance
    }
    return render (request, 'event-detail.html', context )

@login_required
def event_create(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    instance = ""
    if profile.title == "editor":
        form = EventForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            create_action(request.user, 'added  the event', instance)
            created = instance
            print(created)
            if created:
                messages.success(request, "The event \""+str(instance.title)+"\" is created successfully")
            else:
                messages.info(request, "Oops an error occured")
            return HttpResponseRedirect(reverse("admin-event"))
        context = {
             "form": form,
             "instance": instance
        }
    else:
        return redirect(reverse("home"))
    return render (request, 'super/event-form.html', {})

@login_required
def event_update(request, id=None):
    instance = get_object_or_404(Event, id=id)
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.title == "editor":
        form = EventForm(request.POST or None, request.FILES or None, instance=instance)
        print (form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            create_action(request.user, 'Updated the the event', instance)
            created = instance
            print(created)
            if created:
                messages.success(request, "The event \""+str(instance.title)+"\" is succefully updated")
            else:
                messages.info(request, "Oops an error occured")
            return HttpResponseRedirect(reverse("admin-event"))
        context = {
             "form": form,
             "instance": instance
        }
    else:
        return redirect(reverse("home"))
    return render (request, 'super/event-form.html', context)


@login_required
def event_delete(request, id):
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.title == "editor":
        instance = get_object_or_404(Event, id=id)
        instance.delete()
    else:
        return redirect(reverse("home"))
    return redirect(reverse("admin-event"))

@login_required
def admin_events(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.title == "editor":
        event = Event.objects.all()
    else:
        return redirect(reverse("home"))
    return render (request, 'super/admin-event.html', {'events': event })
