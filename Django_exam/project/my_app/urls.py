from django.urls import path
from . import views

urlpatterns = [
    path('', views.regesiter, name='regesiter'),
    path('login', views.login, name='login'),
    path('success', views.success, name='success'),
    path('logout',views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_pie', views.add_pie, name='add_pie'),
    path('edit_pie/<int:id>', views.edit_pie, name='edit_pie'),
    path('delete_pie/<int:id>', views.delete_pie, name='delete_pie'),
    path('all_pie', views.all_pie, name='all_pie'),
    path('view_pie/<int:id>', views.view_pie, name='view_pie'),
]