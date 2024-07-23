from django.urls import path
from . import views

urlpatterns = [
    path('', views.regesiter, name='regesiter'),
    path('login', views.login, name='login'),
    path('success', views.success, name='success'),
    path('logout',views.logout, name='logout'),
]