from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()

#if settings.DEBUG:
#	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)