from django.contrib import admin
from django.urls import path, include
from .views import xyz, abc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', xyz),
    path('App/', abc),
]