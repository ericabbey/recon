from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login,
)


def index(request):
    if not request.user.is_authenticated():
        user = authenticate(username='alby', password='qazwsxedc')
        login(request, user)
        print(request.user)
    return render(request, 'index.html', {})


def about(request):
    print(request.user)
    return render(request, 'about.html', {})
