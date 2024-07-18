from django.db import models

class new_show(models.Model):
    title = models.CharField(max_length=100)
    network=models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    description=models.TextField()
    last_update=models.DateField(auto_now=True)

    def __str__(self):
        return self.title 

def show_all_shows():
    return new_show.objects.all()

def create_show(Tala):
    title = Tala['title']
    network = Tala['network']
    release_date = Tala['release_date']
    description = Tala['description']
    show = new_show(title=title, network=network, release_date=release_date, description=description)
    show.save()
    return show

def read_show(id):
    return new_show.objects.get(id=id)

def update_show(id, title, network, release_date, description):
    show = new_show.objects.get(id=id)
    show.title = title
    show.network = network
    show.release_date = release_date
    show.description = description
    show.save()
    return show

def delete_show(id):
    show = new_show.objects.get(id=id)
    show.delete()

