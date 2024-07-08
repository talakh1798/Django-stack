from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=60)
    age=models.IntegerField()

def get_user(id):
    get=User.objects.get(id=id)
    return get


def create_user(first_name,last_name,email,age):
    User.objects.create(first_name=first_name,last_name=last_name,email=email,age=age)

