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
def delhi(request):
    return render(request,"delhi.html",)
def vrindavan(request):
    return render(request,"vrindavan.html",)
def vaishnodevi(request):
    return render(request,"vaishnodevi.html",)
def agra(request):
    return render(request,"agra.html",)
def mumbai(request):
    return render(request,"mumbai.html",)
def goa(request):
    return render(request,"goa.html",)
def jaishlmair(request):
    return render(request,"jaishlmair.html",)
def jaipur(request):
    return render(request,"jaipur.html",)
def himachal(request):
    return render(request,"himachal.html",)
def lehladakh(request):
    return render(request,"lehladakh.html",)
def kedarnath(request):
    return render(request,"kedarnath.html",)
def shimla(request):
    return render(request,"shimla.html",)
def manali(request):
    return render(request,"manali.html",)




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

        myuser = User.objects.create_user(username,pass1,pass2)
        myuser.email= email

        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"your account has been created.")

        return redirect("signin")
        

    return render(request,"signup.html")


def signin(request):

    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'index.html',{'fname':fname})
        else:
            messages.error(request,"User not found!")
            return redirect('home')    



    return render(request,"signin.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('home')
