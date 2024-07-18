from django.shortcuts import render , redirect
from .models import new_show 
from . import models

# This method for fetching all the shows from the database and rendering them on the template
def show(request):
    shows = models.show_all_shows()   
    return render(request, 'main_show.html', {'shows': shows})  
  
# This method handles the creation of a new show from the database
def create_show(request):
    if request.method == "POST":  
        show = models.create_show(request.POST)
        return redirect('show_detail', id=show.id)
    return render(request, 'create.html')
    
#This method retrieves the details of a specific show from the database using ID
def show_detail(request, id):
    show = models.read_show(id)
    return render(request, 'show_all.html', {'show': show})


# This method is responsible for displaying the edit form for a specific show.
def edit_show_form(request, id):
    show = models.read_show(id)
    return render(request, 'edit_show.html', {'show': show})

# This method updates the details of a specific show.
def update_show(request, id):
    if request.method == "POST":
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        models.update_show(id, title, network, release_date, description)
        return redirect('show_detail', id=id)
    
# This method handles the deletion of a specific show from the database.    
def delete_show(id):
    models.delete_show(id)
    return redirect('show')