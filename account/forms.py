from django import forms
from django.db import models
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            exist = User.objects.filter(username__iexact=username).exists()
            if exist:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError(
                        "The entered password seems incorrect please check "
                    )
            else:
                email_qs = User.objects.all().filter(email__iexact=username)
                if email_qs:
                    username = email_qs[0].username
                    # print(username)
                    user = authenticate(username=username, password=password)
                    if not user:
                        raise forms.ValidationError(
                            "The entered password seems incorrect please check "
                        )
                else:
                    raise forms.ValidationError("This user does not exist")
            if not user.is_active:
                    raise forms.ValidationError(
                        "This user is no longer active."
                    )
        else:
            raise forms.ValidationError(
                "something went wrong please try again"
            )
        if username and not password:
            raise forms.ValidationError(
                "We did not receive any password"
            )
            return username
        return super(loginForm, self).clean(*args, **kwargs)


class registerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        if username:
            usr_exist = User.objects.filter(username__iexact=username).exists()
            if usr_exist:
                raise forms.ValidationError(
                    "A user with that  username already exists."
                )
        return super(registerForm, self).clean(*args, **kwargs)
