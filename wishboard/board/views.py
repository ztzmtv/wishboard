from django.shortcuts import render
from .models import Product


def home(request, category_slug=None):
	products = Product.objects.all()
	return render(request, 'home.html', {'products':products})