from django.conf.urls import url

from .views import dashboard, logout_view, register_view, login_view

urlpatterns = [
        url(r'^dashboard/', dashboard, name="index"),
        url(r'^login/', login_view, name="login"),
        url(r'^register/', register_view, name="register"),
        url(r'^logout/', logout_view, name="logout"),
]
