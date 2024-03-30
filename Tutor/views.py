from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, VideoForm, CommentForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    images = Video.objects.all()
    context = {
        'images': images
    }
    return render(request, 'home.html', context)



def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)



def logoutuser(request):
    logout(request)
    return redirect('login')


def upload_video(request):
    model = Video
    form_class = VideoForm
    form = VideoForm()
    data = Video.objects.all()
    category = Category.objects.all

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()

    context = {
        'form': form,
        'data': data,
    }

    return render(request, 'upload.html', context)


def video_view(request, pk):
    photo = Video.objects.get(id=pk)
    model = Comment
    form = CommentForm()
    form_class = CommentForm
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm()
    context = {
        'photo': photo,
        'form': form,
        'comments': comments
    }
    return render(request, 'view.html', context)



# Create your views here.
