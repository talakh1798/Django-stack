from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=50)

class Ninja(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dojo = models.ForeignKey(Dojo, related_name="Ninjas", on_delete=models.CASCADE)


def create_dojo(name,city,state):
   Dojo.objects.create(name=name,city=city,state=state)


def create_ninja(first_name,last_name,dojo):
   Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=dojo)

# def get_to_delete(id):
#  return Dojo.objects.get(id=id)
 
