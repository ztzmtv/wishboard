from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Product

class AddProductForm(forms.Form):
    name = forms.CharField(label='Название', required=True, help_text='Название')
    description = forms.CharField(widget=forms.Textarea, help_text='Описание', required=False)
    image = forms.ImageField(help_text='Изображение', required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0, help_text='Цена (не обязвательно)', required=False)
    link = forms.URLField(label='URL', required=False)
    is_granted = forms.BooleanField(required=False)
    is_public = forms.BooleanField( required=False)

# class AddProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'image', 'price', 'link', 'is_granted', 'is_public']
