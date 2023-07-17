from django.shortcuts import render,redirect
# from .models import Student,Recruiter

# Create your views here.
def postjob(request):
    return render(request,"siteone/home.html", {})
