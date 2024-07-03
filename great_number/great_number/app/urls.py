from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('great_number/',views.guess,name='great_number'),
    path('reset/',views.reset,name='reset')
]
