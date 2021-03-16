from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import AddProductForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime


def home(request):
    products = Product.objects.all()
    add_product_form = AddProductForm(request.POST, request.FILES)
    return render(
        request,
        "home.html",
        {"products": products, "add_product_form": add_product_form},
    )


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
    return render(request, "home.html", {"add_product_form": add_product_form})
