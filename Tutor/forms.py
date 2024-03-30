from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Video, Comment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video', 'category', 'image', 'video_name')

        widgets = {
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'video_name')

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'video_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
