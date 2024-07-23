from django.db import models
from datetime import datetime
from django.utils import timezone
import re

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

        # registered email should be unique
        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email address already exists."

        # Add a date field and validate that the user's birthday is in the past
        date = datetime.strptime(postData['date'], '%Y-%m-%d')
        if date > datetime.now():
            errors["date"] = "date should be in the past" 

        # Add a birthday field and validate that the user is at least 13 years old 
        current_year = datetime.now().year
        age = current_year - date.year
        if age < 13:
            errors["age"] = "User must be at least 13 years old." 
        
        return errors    


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    

    def __str__(self):
        return self.first_name + " " + self.last_name
    
def create_account(request,pw_hash) :
    first_name=request['first_name']
    last_name=request['last_name']
    email=request['email']
    password=request['password']
    confirm_password=request['confirm_password']
    date=request['date'] 
    
    return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash, confirm_password=pw_hash,date=date)



