from django.db import models
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

class Pie(models.Model):
    name = models.CharField(max_length=50)
    filling = models.CharField(max_length=50)
    crust = models.CharField(max_length=50)
    baker = models.ForeignKey(User,related_name="bakers",on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def read_all_pies():
    return Pie.objects.all()

def create_pie(name,filling,crust,baker):
    return Pie.objects.create(name=name, filling=filling, crust=crust,baker=baker)

def update_pie(id, name, filling, crust):
    pie = Pie.objects.get(id=id)
    pie.name = name
    pie.filling = filling
    pie.crust = crust
    pie.save()
    return pie

def delete_pie(id):
    pie = Pie.objects.get(id=id)
    pie.delete()
    return pie

def create_account(request,pw_hash) :
    first_name=request['first_name']
    last_name=request['last_name']
    email=request['email']
    confirm_password=request['confirm_password'] 
    password=request['password']
    date=request['date'] 
    
    return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash, confirm_password=pw_hash,date=date)






# Create your models here.
