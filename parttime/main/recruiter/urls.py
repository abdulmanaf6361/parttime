from django.urls import path
from .views import *

urlpatterns = [
    path("",postjob),
    path("postjob/",postjob),
]
