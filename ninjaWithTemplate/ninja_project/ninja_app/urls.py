from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_dojo ),
    path('pluse', views.add_ninja ),
#     path('delete', views.delete_dojo)
 ]