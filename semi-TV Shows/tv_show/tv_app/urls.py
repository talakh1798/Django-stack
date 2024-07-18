from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.show, name="show"),
    path('shows/new/', views.create_show, name="create_show"),
    path('shows/<int:id>/', views.show_detail, name="show_detail"),
    path('shows/<int:id>/edit/', views.edit_show_form, name="edit_show_form"),
    path('shows/<int:id>/update/', views.update_show, name="update_show"),
    path('shows/<int:id>/destroy/', views.delete_show, name="delete_show"),
]


