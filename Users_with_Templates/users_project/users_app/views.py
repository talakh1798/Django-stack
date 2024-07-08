from django.shortcuts import render,redirect,HttpResponse
from . import models
from .models import User

def index(request):
    models.get_user(id=1)
    context={
        "all_users":User.objects.all()
    }
    return render(request,'add_user.html', context)    
    

def add(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        age=request.POST['age']

        models.create_user(first_name=first_name,last_name=last_name,email=email,age=age)
        return redirect('users/')
    return render(request,'add_user.html')


