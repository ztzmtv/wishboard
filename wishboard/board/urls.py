from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-product", views.add_product, name="add-product"),
    path("account/create/", views.signup_view, name="signup"),
    path("account/login/", views.login_view, name="login"),
    #    path('add/<int:product_id>', views.add_product(), name='add_product'),
]

urlpatterns += [
    re_path(r"^wish/(?P<pk>[-\w]+)/renew/$", views.add_product, name="renew-wish"),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
