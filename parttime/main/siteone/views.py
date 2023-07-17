from django.shortcuts import render,redirect
from .models import Student,Recruiter

# Create your views here.
def home(request):
    return render(request,"siteone/home.html", {})

def student_signup(request):
    if request.method=='POST':
        print("Added")
        #retreive the user inputs 
        name=request.POST.get("name")
        college=request.POST.get("college")
        current_location=request.POST.get("location")
        email=request.POST.get("email")
        password=request.POST.get("password")
        rpt_password=request.POST.get("rpt_password")
        city=request.POST.get("city")
        phone=request.POST.get("phone")

        #create an object for models 
        if(password==rpt_password):
            s=Student()
            s.name=name
            s.college=college
            s.current_location=current_location
            s.email=email
            s.password=password
            s.city=city
            s.phone=phone

            s.save()
            return redirect("/home/")
        return render(request,"siteone/student_signup.html", {})
        

    return render(request,"siteone/student_signup.html", {})





def recruiter_signup(request):
    if request.method=='POST':
        print("Recruiter Added")
        #retreive the user inputs 
        name=request.POST.get("name")
        organization=request.POST.get("organization")
        current_location=request.POST.get("location")
        email=request.POST.get("email")
        password=request.POST.get("password")
        rpt_password=request.POST.get("rpt_password")
        city=request.POST.get("city")
        phone=request.POST.get("phone")

        #create an object for models 
        if(password==rpt_password):
            r=Recruiter()
            r.name=name
            r.organization=organization
            r.current_location=current_location
            r.email=email
            r.password=password
            r.city=city
            r.phone=phone

            r.save()
            return redirect("/home/")
        return render(request,"siteone/recruiter_signup.html",{})
        

    return render(request,"siteone/recruiter_signup.html", {})




def recruiter_login(request):
    if request.method=='POST':
        print("Recruiter login")
        #retreive the user inputs 
        
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        try:
            user = Recruiter.objects.get(email=email, password=password)
            # Login successful
            # Perform any desired actions or redirect to a success page
            return redirect("/home/")
        except Recruiter.DoesNotExist:
            # Login failed
            # Render the login page with an error message
            error_message = 'Invalid email or password.'
            return render(request, 'siteone/recruiter_login.html', {'error_message': error_message})


       
        #     return redirect("/home/")
        # return render(request,"siteone/recruiter_signup.html",{})
        

    return render(request,"siteone/recruiter_login.html", {})


def student_login(request):
    if request.method=='POST':
        print("Student login")
        #retreive the user inputs 
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        try:
            user = Student.objects.get(email=email, password=password)
            # Login successful
            # Perform any desired actions or redirect to a success page
            return redirect("/home/")
        except Student.DoesNotExist:
            # Login failed
            # Render the login page with an error message
            error_message = 'Invalid email or password.'
            return render(request, 'siteone/student_login.html', {'error_message': error_message})

            

    return render(request,"siteone/student_signup.html", {})
