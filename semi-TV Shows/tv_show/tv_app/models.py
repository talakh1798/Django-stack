from django.db import models
from datetime import datetime
import re

class TvShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network should be at least 3 characters"
        if len(postData['description']) < 10 :
            errors["description"] = "description should be at least 10 characters"
        #check if release date is in past date format
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", postData['release_date']):
            errors["release_date"] = "release date should be in YYYY-MM-DD format" 
        #check if release date is in the past     
        release_date = datetime.strptime(postData['release_date'], '%Y-%m-%d')
        if release_date > datetime.now():
            errors["release_date"] = "release date should be in the past"    
        return errors
    
   
class new_show(models.Model):
    title = models.CharField(max_length=100)
    network=models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    description=models.TextField()
    last_update=models.DateField(auto_now=True)
    objects = TvShowManager()  # Create a custom manage

    def __str__(self):
        return self.title 

# get all objects from the database and return a list of objects that match 
def show_all_shows():
    return new_show.objects.all()

# create a new TvShow object with the given title and description and release date and network
def create_show(Tala):
    title = Tala['title']
    network = Tala['network']
    release_date = Tala['release_date']
    description = Tala['description']
    show = new_show(title=title, network=network, release_date=release_date, description=description)
    show.save()
    return show


# retrieve a TvShow object with the given id and return it
def read_show(id):
    return new_show.objects.get(id=id)


# update a TvShow object with the given id and new title, description, and release date and network
def update_show(id, title, network, release_date, description):
    show = new_show.objects.get(id=id)
    show.title = title
    show.network = network
    show.release_date = release_date
    show.description = description
    show.save()
    return show

# delete a TvShow object with the given id from the database
def delete_show(id):
    show = new_show.objects.get(id=id)
    show.delete()

