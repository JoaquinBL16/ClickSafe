from django.urls import path, include
from .views import index
from django.conf import settings

urlpatterns = [
    path('', index, name="index"),

]

