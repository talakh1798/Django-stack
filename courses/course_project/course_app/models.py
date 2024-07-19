from django.db import models


class CourseManager(models.Manager):
   def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "course name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors["description"] = "course description should be at least 15 characters"
        return errors

# class Description(models.Model):
#     content=models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    # description =models.OneToOneField(Description,related_name='courses',on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

# this method for creating a new Course object from the database    
def create_course(request):
    name = request['name']
    description = request['description']
    return Course.objects.create(name=name, description=description)
    
# this method for getting objects from the database 
def get_course():
    return Course.objects.all()


# this method for deleting a course object from the database
def delete_course(id):
    course = Course.objects.get(id=id)
    course.delete()


