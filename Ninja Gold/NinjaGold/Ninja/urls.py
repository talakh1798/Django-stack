from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.page),
    path('process_money',views.process,name="process_money"),
]
