from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_page,name='course_page'), 
    path('add_course', views.add_course, name='add_course'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'), 
]