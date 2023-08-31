"""PizzaDelivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home,adminloginview,adminhome,adminauth,adminlogout,addPizza,deletePizza

urlpatterns = [
    path('', home,name="homepage"),
    path('admin/',adminloginview,name="adminloginpage"),
    path('admin/authenticate/',adminauth),
    path('admin/home',adminhome,name="adminhomepage"),
    path('adminlogout/',adminlogout,name="adminlogout"),
    path('addpizza/',addPizza,name="addPizza"),
    path('deletepizza/<int:pizza_id>',deletePizza,name="deletePizza"),
    
]
