from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate ,login,logout

# Create your views here.
def index(request):
    context={
        "variable":"perfect"
    }

    return render(request,"index.html",context)
    # return HttpResponse("This is homepage")

def topplaces(request):
    # return HttpResponse("This is aboutpage")
    return render(request,"topplaces.html",) 

def hotel(request):
    # return HttpResponse("This is servicespage")
    return render(request,"hotel.html",)
def places(request):
    return render(request,"places.html",)




def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = Contact(name =name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        
        messages.success(request,'your message has been sent')

        return redirect("home")

    # return HttpResponse(7082811161)
    
    
    return render(request,"contact.html",)

def signup(request):

    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1,pass2)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"your account has been created.")

        return redirect("login")
        

    return render(request,"signup.html")


def login(request):

    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.firstname
            return render(request,'index',{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')    



    return render(request,"login.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('home')
