from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("account/create/", views.signup_view, name="signup"),
    path("account/login/", views.login_view, name="login"),
]
