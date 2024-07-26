from django.shortcuts import render,redirect
from .models import User ,Pie
from . import models
from django.contrib import messages
import bcrypt

# this function to creating a new instance of User object from the database and returning it 
# validation error message from the database when validation fails and the user is invalid 
# bycrption of the password 
def regesiter(request):
    if request.method == "POST" : 
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)
            user=models.create_account(request.POST,pw_hash=pw_hash)
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('/')
    return render(request,'login_form.html')


# this function to validate the user login and return the user object when the login is valid
def login(request):
    if request.method == "POST" :
        email=request.POST['email']
        password=request.POST['password']
        user = User.objects.filter(email=email).first()
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if user and bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('success')
        else:
            return render(request,'login_form.html', {'error': 'Invalid email or password'})


# this function to display the success page when the user is logged in 
def success(request):
    first_name=request.session['first_name']
    last_name=request.session['last_name']
    context={
        'first_name':first_name,
        'last_name':last_name,  # sending the user's name to the template for display  
    }
    return render(request,'dashboard.html' ,context)


# this function to destroy the session and redirect to the login page when the user is logged out
def logout(request):
    request.session.clear()
    # request.session.flush()
    return redirect('/')


# this function to display the dashboard page with all the pies when the user is logged in
def dashboard(request):
    first_name=request.session['first_name']
    last_name=request.session['last_name']
    pies = models.read_all_pies()
    return render(request, 'dashboard.html', { 'pies': pies  , 'first_name': first_name, 'last_name': last_name})


# this function to display the form to add a new pie when the user is logged in
def add_pie(request):
    first_name=request.session['first_name']
    last_name=request.session['last_name']
    pies = models.read_all_pies()
    if request.method == "POST":
        name = request.POST['name']
        filling = request.POST['filling']
        crust = request.POST['crust']
        baker = User.objects.get(id=request.session['id'])
        if not name or not filling or not crust:
            messages.error(request, 'Please fill all fields!')
            return redirect('dashboard')
        else:
            models.create_pie(name, filling, crust, baker)
            messages.success(request, 'Pie added successfully!')   
            return redirect('dashboard')
    return render(request, 'dashboard.html' , {'pies': pies ,'first_name': first_name, 'last_name': last_name})


# this function to display the form to edit an existing pie 
def edit_pie(request, id):
    pie = models.Pie.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        filling = request.POST['filling']
        crust = request.POST['crust']
        if not name or not filling or not crust:
            messages.error(request, 'Please fill all fields!')
            return redirect('edit_pie' , id=id)
        else: 
            models.update_pie(id, name, filling, crust)
            return redirect('dashboard')
    return render(request, 'edit_pie.html', {'pie': pie})


# this function to delete an existing pie 
def delete_pie(request, id):
    pie = models.Pie.objects.get(id=id)
    pie.delete()
    messages.success(request, 'Pie deleted successfully!')
    return redirect('dashboard')


# this function to display all the pies , and we can go to view pie data from name pie
def all_pie(request):
    first_name=request.session['first_name']
    pies = models.read_all_pies()
    return render(request, 'all_pies.html', {'pies': pies , 'first_name':first_name})


# this function to display the form to view an existing pie (pie data)
def view_pie(request, id):
    pie = models.Pie.objects.get(id=id)
    first_name=request.session['first_name']
    return render(request, 'view_pie.html', {'pie': pie, 'first_name': first_name})













   

 



        
        





