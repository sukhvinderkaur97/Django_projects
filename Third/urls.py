from django.contrib import admin
from django.urls import path, include
from .views import pqr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pqr),
]