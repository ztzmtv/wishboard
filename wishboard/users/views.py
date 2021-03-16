from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name="User")
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"signup_form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return redirect("signup")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"login_form": form})
