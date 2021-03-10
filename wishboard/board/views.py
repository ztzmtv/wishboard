from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import AddProductForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    products = Product.objects.all()
    form = AddProductForm(request.POST, request.FILES)
    return render(request, 'home.html', {'products': products, 'form': form})


def add_product(request):
    #    product = Product()
    if request.method == 'POST':
        add_product_form = AddProductForm(request.POST, request.FILES)
        if add_product_form.is_valid():
            #            product_ = form.save(commit=False)
            # add_product_form.save(commit=False)
            product = Product(name=add_product_form.cleaned_data['name'],
                              description=add_product_form.cleaned_data['description'],
                              image=add_product_form.cleaned_data['image'],
                              price=add_product_form.cleaned_data['price'],
                              link=add_product_form.cleaned_data['link'],
                              is_granted=add_product_form.cleaned_data['is_granted'],
                              is_public=add_product_form.cleaned_data['is_public'], )
            product.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        add_product_form = AddProductForm(request.POST, request.FILES)
    return render(request, 'home.html', {'form': add_product_form})
