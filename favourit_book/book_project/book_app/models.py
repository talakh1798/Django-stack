from django.db import models
import re
from datetime import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters long."

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters long."

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."
        
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters long."
            
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match."

        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email already exists."
        return errors    

    def update(self, postData):
        errors={}
        if len(postData['title']) < 5:
            errors['title'] = "Title should be at least 5 characters long."

        if Book.objects.filter(title = postData['title']).exists():
            errors['title'] = "Title is exsist"

        if len(postData['description']) < 5:
            errors['description'] = "Description should be at least 5 characters long."
 
        return errors    

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_uploaded = models.ForeignKey(User, related_name='books_uploaded', on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name='liked_books')


    def __str__(self):
        return self.title
    
def create_account(request,pw_hash):
    first_name=request['first_name']
    last_name=request['last_name']
    email=request['email']
    password=request['password']
    confirm_password=request['confirm_password']
    return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash, confirm_password=pw_hash)

def create_book( title ,description, id):
    user = User.objects.get(id = id )
    books = Book.objects.create( title = title , description=description ,book_uploaded=user)
    books.users_who_like.add(user)
   

def read_all_book():
    return Book.objects.all()

def update_book(id, title, description):
    book=Book.objects.get(id=id)
    # book.title=title
    book.description=description
    book.save()
    return book
    
def read_book(id):
    return Book.objects.get(id=id)

def delete_book(id):
    book=Book.objects.get(id=id)
    book.delete()
    return book







