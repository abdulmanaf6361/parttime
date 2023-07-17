from django.shortcuts import render,redirect
from .models import modelsignup,description
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    # std=Student.objects.all()
    if request.method=='POST':
        desc=request.POST.get("description")
        description_obj=description()
        description_obj.description=desc
        
        description_obj.save()
        
        return redirect("/mainapp/success/")
    

    return render(request,"home.html", {})

def success(request):
    # std=Student.objects.all()

    return render(request,"success.html", {})
def signup(request):
    if request.method=='POST':
        print("added")
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        rptpassword=request.POST.get("rpt-password")
        
        s=modelsignup()
        s.name=name
        s.email=email
        s.password=password
        
        s.save()
        return redirect("/mainapp/signup/")
    return render(request,"signup.html",{})


def login(request):
    if request.method=='POST':
        print("login")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        try:
            user = modelsignup.objects.get(email=email) 
            if user.password == password:
                return profile(request,user)
            else:
                error_message = "Incorrect password. Please try again."
        except modelsignup.DoesNotExist:
            error_message = "Email address not found. Please try again."
        print("brooooo ",error_message)
        
        # return redirect("/mainapp/success/")
    return render(request,"login.html",{})


def profile(request,user):
    return render(request,"profile.html", {'user':user})

def profile(request):
    return render(request,"login.html", {})



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         profile = modelsignup.objects.get(email=request.email)
#         profile.name = request.POST['name']
#         profile.email = request.POST['email']
#         profile.password = request.POST['password']
#         profile.save()
#         return redirect('profile')

#     profile = modelsignup.objects.get(email=request.email)
#     context = {'profile': profile}
#     return render(request, 'profile.html', context)
