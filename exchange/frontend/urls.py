from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from .views import index


urlpatterns = [
    path('', index),
    path('create', index),
]
