from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "publish"
        ]


class CommentForm(forms.Form):
    blog = forms.CharField(widget=forms.HiddenInput)
    content = forms.CharField(widget=forms.Textarea, label="")
