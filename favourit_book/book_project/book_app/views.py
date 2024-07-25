from django.shortcuts import render,redirect
from .models import User , Book
from . import models
from django.contrib import messages
import bcrypt


def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
        else:        
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)
            user=models.create_account(request.POST,pw_hash=pw_hash)
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
            return redirect('/')
    return render(request, 'login_form.html')

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email).first()
        if user and bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['id']= user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
            return redirect('/')
    return render(request, 'add_book.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book(request):
    user_id =request.session['id']
    first_name=request.session['first_name']
    last_name=request.session['last_name']
    books=Book.objects.all()
    if request.method == 'POST':
        errors = User.objects.update(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
             messages.error(request, value)
            return redirect('add_book')
        else:
            title = request.POST['title']
            description = request.POST['description']
            models.create_book(title, description, id=user_id)
    return render(request, 'add_book.html', {'books':books , 'first_name':first_name, 'last_name':last_name})
   
def update_book(request, id):
    first_name=request.session['first_name']
    last_name=request.session['last_name']
    user_id = request.session.get('id')
    user = User.objects.get(id=user_id)
    book = models.read_book(id)
    if request.method == 'POST':
        print("POST data:", request.POST)
        if 'title' in request.POST:
            title = request.POST['title']
            models.update_book(id, title)      
        description = request.POST['description']
        models.update_book(title=None ,description=description,id=id )
    return render(request, 'update.html', {'book': book, 'first_name': first_name, 'last_name': last_name})

def delete_book(request,id):
    if request.method == 'POST':
        id = request.POST['id']
    models.delete_book(id=id)
    return redirect('add_book')

def favorite_book(request):
    if request.method == 'POST':
        id = request.POST['id']
        book = models.Book.objects.get(id=id)
        user_id = request.session.get('id')
        user = User.objects.get(id=user_id)
        book.users_who_like.add(user)
        return redirect('add_book')

def unfavorite_book(request):
    if request.method == 'POST':
        id = request.POST['id']
        book = models.Book.objects.get(id=id)
        user_id = request.session.get('id')
        user = User.objects.get(id=user_id)
        book.users_who_like.remove(user)
        return redirect('add_book')
    
    

# def info_book(request,id):
#     book=models.read_book(id)
#     first_name=request.session['first_name']
#     last_name=request.session['last_name']
#     return render(request, 'info.html', {'book': book, 'first_name': first_name, 'last_name': last_name})







   

