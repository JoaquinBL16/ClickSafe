from django.urls import path, include
from .views import login 
from django.conf import settings

urlpatterns = [
    path('', login, name="login"),

]

