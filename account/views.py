from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect, get_object_or_404

from blogs.models import Post, like, Comment
from .forms import loginForm, registerForm
from .models import UserProfile, Action, Chat
from .utils import create_action


login_required(login_url='login')
def dashboard(request):
    profile = UserProfile.objects.filter(title="editor").exclude(user=request.user)
    user_p = get_object_or_404(UserProfile, user=request.user)
    instance = Post.objects.filter(user=request.user)
    if user_p.title == "editor":
        lik = like.objects.filter(blog=instance)
        com = Comment.objects.filter(blog=instance)
        actions = Action.objects.exclude(user=request.user)
        actions = actions.select_related('user', 'user__userprofile')\
                         .prefetch_related('target')
        actions = actions[:6]
        c = Chat.objects.all()
        context ={
        'post': instance,
        'like': lik,
        'profile': profile,
        'actions': actions,
        'chat': c
        }
    else:
        return redirect(reverse("home"))
    return render (request, 'super/index.html', context)


def post(request):
    if request.method == 'POST':
        msg = request.POST.get('msgbox', None)
        rcvr = request.POST.get('receiver', None)
        receiver = User.objects.get(username=rcvr)
        c = Chat(sender=request.user, receiver=receiver, message=msg)
        if msg != "":
            c.save()
            return JsonResponse({'msg': msg, 'receiver': rcvr})
    else:
        return HttpResponse('Request must be post')


def message(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})


def login_view(request):
    nxt = request.GET.get('next', 'super:index')
    form = loginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if nxt:
            return redirect(nxt)
        print(request.user.is_authenticated())
    return render(request, "login_form.html", {"form": form})


def register_view(request):
    form = registerForm(request.POST or None)
    nxt = request.GET.get('next', 'home')
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        new_profile, created = UserProfile.objects.get_or_create( user=request.user, title="normal")
        create_action(request.user, "Created an account")
        if nxt:
            return redirect(nxt)

    context = {
        "form": form
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')
