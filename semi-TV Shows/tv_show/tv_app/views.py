from django.shortcuts import render , redirect
from .models import new_show, TvShowManager 
from django.contrib import messages
from . import models 

def create_show(request):
    if request.method == "POST":
        # errors = new_show.objects.basic_validator(request.POST)
        errors=models.new_show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            # Pass the POST data back to the form
            return render(request, 'create.html')
        # title is unique
        elif new_show.objects.filter(title=request.POST['title']):
            messages.error(request, "Title already exists")
            return render(request, 'create.html')
        else:
            show=models.create_show(request.POST)
            messages.success(request, "TvShow successfully created")
            return redirect('show_detail', id=show.id)
    return render(request, 'create.html')

# This method for fetching all the shows from the database and rendering them on the template
def show(request):
    shows = models.show_all_shows()   
    return render(request, 'main_show.html', {'shows': shows})  
  
    
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
        # errors=models.new_show.objects.basic_validator(request.POST)
        errors=new_show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            # Pass the POST data back to the form
            return render(request, 'edit_show.html', {'show': models.read_show(id)})
        else:
            models.update_show(id, request.POST['title'], request.POST['network'], request.POST['release_date'], request.POST['description'])
            messages.success(request, "TvShow successfully updated")
            return redirect('show_detail', id=id)
    return render(request, 'edit_show.html', {'show': models.read_(id)})    
        
                    
            
# This method handles the deletion of a specific show from the database.    
def delete_show(request,id):
    models.delete_show(id)
    return redirect('show')