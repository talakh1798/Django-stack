
from django.urls import path
from . import views

urlpatterns = [
    path('',views.count_time),
    path('destroy_session',views.destroy_session,name='destroy_session'),
    path('add',views.add,name='add')
]