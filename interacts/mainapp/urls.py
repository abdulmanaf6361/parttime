from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("signup/",signup),
    path("login/",login),
    path("success/",success),
    path("profile/",profile),
]
