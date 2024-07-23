from django.shortcuts import render,redirect
from .models import User
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
    return render(request,'success.html' ,{'first_name':first_name,'last_name':last_name})


# this function to destroy the session and redirect to the login page when the user is logged out
def logout(request):
    request.session.clear()
    # request.session.flush()
    return redirect('/')
   

 



        
        


