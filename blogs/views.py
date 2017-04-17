from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404,redirect

from account.utils import create_action
from account.models import UserProfile
from .forms import PostForm, CommentForm
from .models import Post, Comment, like

today = datetime.now().strftime("%Y-%m-%d")


@login_required(login_url='/login/')
def post_create(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile.title)
    if profile.title == "editor":
        if not request.user.is_authenticated:
            raise Http404
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            if str(instance.publish) != today:
                instance.draft = True
            else:
                instance.draft = False
            instance.save()
            create_action(request.user, 'posted the message', instance)
            created = instance
            print(created)
            if created:
                if not instance.draft:
                    messages.success(request, "The blog \""+str(instance.title)+"\" is created succefully and we live")
                else:
                    messages.success(request, "The blog \""+str(instance.title)+"\" is save succefully")
            else:
                messages.info(request, "Oops an error occured")
            return HttpResponseRedirect(reverse("admin-blog"))
        context = {
             "form": form,
             "instance": ""
        }
    else:
        return redirect('home')
    return render(request, "super/post-form.html", context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    com_user = get_object_or_404(User, id=request.user.id),
    initial_data = {
        'blog': instance,
        'user':com_user
    }
    if request.is_ajax():
        blog_id = request.POST.get("blog-id")
        print(blog_id)
        vote = like.objects.filter(blog=instance, user=request.user)
        if vote.exists():
            vote.delete()
            count = instance.like_set.count()
            return JsonResponse({'count': str(count)} )
        else:
            new_like,created = like.objects.get_or_create(blog=instance, user=request.user)
            count = instance.like_set.count()
            create_action(request.user, 'likes', new_like)
            return JsonResponse({'count':   count})

    form = CommentForm(request.POST or None, initial=initial_data)
    current_user = request.user.id
    detail_url = request.path
    if form.is_valid():
        c_type = instance
        user = request.user
        content_data = form.cleaned_data.get('content')
        new_comment, created = Comment.objects.get_or_create(
            user=user,
            blog=c_type,
            content=content_data,
        )
        create_action(request.user, 'commented on your post', new_comment)
        return HttpResponseRedirect('/')

    context = {
        'instance': instance,
        'form': form,
        'current_user': current_user,
        'path': detail_url
    }
    return render(request, "blog_detail.html", context)


def post_list(request):
    queryset = Post.objects.exclude(draft=True)  # .order_by("-timestamp")
    # profile = UserProfile.objects.filter(user=request.user)
    query = request.GET.get("q")
    current_user = request.user.id
    if query:
        queryset = queryset.filter(Q(title__icontains=query) | Q(author__icontains=query)).distinct()
    obj_count = queryset.count()
    context = {
        "object_list": queryset,
        "title": "list",
        "current_user": current_user,
        # "pro": profile,
        'obj_count': obj_count
    }
    return render(request, "blogs.html", context)


@login_required(login_url='login')
def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    profile = get_object_or_404(UserProfile, user=request.user)
    today = datetime.now().strftime("%Y-%m-%d")
    if profile.title == "editor":
        form = PostForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            if str(instance.publish) <= today:
                instance.draft = False
            else:
                instance.draft = True
            instance.save()
            create_action(request.user, 'Updated the blog', instance)
            created = instance
            print(created)
            if created:
                messages.success(request, "The blog \""+str(instance.title)+"\" is succefully updated")
            else:
                messages.info(request, "Oops an error occured")
            return HttpResponseRedirect(reverse("admin-blog"))
        context = {
             "form": form,
             "instance": instance
        }
    else:
        return redirect('home')
    return render(request, "super/post-form.html", context)


@login_required(login_url='login')
def post_delete(request, id):
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.title == "editor":
        instance = get_object_or_404(Post, id=id)
        instance.delete()
    else:
        return redirect(reverse("home"))
    return redirect("posts:list")


@login_required(login_url='login')
def admin_post(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.title == "editor":
        queryset = Post.objects.all().filter(user=request.user)
    else:
        return redirect(reverse("home"))
    context = {
        'qs': queryset
    }
    return render(request, 'super/admin-post.html', context)
