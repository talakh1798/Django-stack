from django.shortcuts import render,redirect
from.models import Course
from . import models
from django.contrib import messages

# this function to get the current course  object from the database and return 
def course_page(request):
    courses = models.get_course()
    return render(request, 'course_page.html', {'courses': courses})


# this function to handle adding new course to the database 
def add_course(request):
    if request.method == 'POST':
    # errors = Course.objects.basic_validator(request.POST)
        errors=models.Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('course_page')
        else:
            models.create_course(request.POST)
            return redirect('course_page')
    return render(request, 'course_page.html')

# this function to delete a course from the database and return redirect back to course page 
def delete_course(request,id):
   course = models.Course.objects.get(id=id)
   if request.method == 'POST':
       models.delete_course(id)
        # redirect to the course_page view after deletion
       return redirect('course_page')
   return render(request, 'delete_course.html', {'course': course})
        
      

