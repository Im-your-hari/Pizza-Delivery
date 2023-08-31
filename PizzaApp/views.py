from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def adminloginview(request):
    return render(request,'admin.html')

def adminauth(request):
    name = request.POST['username']
    pswd = request.POST['password']
    user = authenticate(username=name, password=pswd)

    if user is not None:
        login(request, user)
        messages.add_message(request,messages.SUCCESS,"Login Success..!")
        return redirect('adminhomepage')


    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials..!")
        return redirect('adminloginpage')

def adminhome(request):
    return render(request, 'adminhome.html')

def adminlogout(request):
    logout(request)
    return redirect('adminloginpage')
