from django.contrib import admin
from django.urls import path, include
from .views import xyz, abc, pqr, lmn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', xyz),
    path('second/', abc),
    path('third/', pqr,  name = "temp1"),
    path('fourth/', lmn,  name = "temp2"),
]
