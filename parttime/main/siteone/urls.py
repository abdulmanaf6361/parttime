from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("student_signup/",student_signup),
    path("recruiter_signup/",recruiter_signup),
    path("student_login/",student_login),
    path("recruiter_login/",recruiter_login),
]
