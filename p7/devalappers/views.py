from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from . models import Customer , Invoice

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    return HttpResponse("this is our contact")

def signin(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already registered')
                return redirect('signin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                return redirect('signin')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Confirm Password did not mathch")
            return redirect('signin')




    return render(request,"signup.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request ,User)
            return redirect('/')
        else:
             messages.info(request,'Invalid Credentials')
             return redirect('login')


    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def invoice(request):
    data = Invoice.objects.all()
    params = {'invoice_id': data }



    return render(request,'invoice.html',params)

def wallet(request):
    return HttpResponse("this is wallet")

def outstanding(request):
    return HttpResponse("this is outstanding ")

def advancepay(request):
    return HttpResponse("this is advance pay ")
