from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PizzaModel

# Create your views here.
def home(request):
    context = {'pizza' : PizzaModel.objects.all()}
    return render(request,'index.html',context)

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
    context = {'pizza' : PizzaModel.objects.all()}
    return render(request, 'adminhome.html',context)

def adminlogout(request):
    logout(request)
    return redirect('adminloginpage')


def addPizza(request):
    pizzaname = request.POST['pizza-name']
    pizzaprice = request.POST['pizza-price']
    pizzadescribe = request.POST['pizza-describe']

    PizzaModel(name=pizzaname,price=pizzaprice,description=pizzadescribe).save()
    return redirect('adminhomepage')

def deletePizza(request,pizza_id):
    PizzaModel.objects.filter(id=pizza_id).delete()
    return redirect('adminhomepage')