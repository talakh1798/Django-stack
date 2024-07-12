from django.shortcuts import render,redirect
from . import models
from .models import Dojo , Ninja


def index(request):
  
    context ={
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        Dojo.objects.create(name=name, city=city, state=state)
    return redirect('/')


def add_ninja(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        id = request.POST['dojo_id']
        dojo = Dojo.objects.get(id=id)
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/')

# def delete_dojo(request):
#     if request.method == 'POST':
#         dojo_id = request.POST['dojo_id']
#         dojo = Dojo.get_to_delete(dojo_id)
#         dojo.delete()
#     return redirect('/')
# Create your views here.
