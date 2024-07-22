from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('pfapp.urls')),
    path('customadmin/', admin.site.urls)
]
