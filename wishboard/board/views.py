from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import AddProductForm, SignUpForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def home(request):
    products = Product.objects.all()
    form = AddProductForm(request.POST, request.FILES)
    return render(request, "home.html", {"products": products, "form": form})


def add_product(request):
    if request.method == "POST":
        add_product_form = AddProductForm(request.POST, request.FILES)
        if add_product_form.is_valid():
            product = Product(
                name=add_product_form.cleaned_data["name"],
                description=add_product_form.cleaned_data["description"],
                image=add_product_form.cleaned_data["image"],
                price=add_product_form.cleaned_data["price"],
                link=add_product_form.cleaned_data["link"],
                is_granted=add_product_form.cleaned_data["is_granted"],
                is_public=add_product_form.cleaned_data["is_public"],
                added_by=request.user,
                created=datetime.now(),
                updated=datetime.now(),
            )
            product.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        add_product_form = AddProductForm(request.POST, request.FILES)
    return render(request, "home.html", {"form": add_product_form})


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
    return render(request, "signup.html", {"signup_form": form})


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
    return render(request, "login.html", {"login_form": form})
