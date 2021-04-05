from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-product", views.add_product, name="add-product"),
    path("product/<int:pk>", views.show_product, name="product-details"),
]

urlpatterns += [
    #    re_path(r"^product/<int:pk>", views.show_product, name="product-details"),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
