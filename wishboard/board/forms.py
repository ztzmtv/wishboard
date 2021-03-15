from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Product
from django.contrib.auth.forms import UserCreationForm


class AddProductForm(forms.Form):
    name = forms.CharField(label="Название", required=True, help_text="Название")
    description = forms.CharField(
        label="Описание", widget=forms.Textarea, help_text="Описание", required=False
    )
    image = forms.ImageField(
        label="Изображение", help_text="Изображение", required=False
    )
    price = forms.DecimalField(
        label="Цена",
        max_digits=10,
        decimal_places=2,
        min_value=0,
        help_text="Цена (не обязвательно)",
        required=False,
    )
    link = forms.URLField(label="URL", required=False)
    is_granted = forms.BooleanField(label="Исполнено", required=False)
    is_public = forms.BooleanField(label="Публичное", required=False)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text="eg.youremail@email.com")

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
            "email",
        )
