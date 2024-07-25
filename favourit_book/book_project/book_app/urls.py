from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'), 
    path('login',views.login, name='login'),
    path('logout', views.logout, name='logout'), 
    path('add_book',views.add_book, name='add_book'),
    path('update_book/<int:id>',views.update_book, name='update_book'),
    path('delete_book/<int:id>',views.delete_book, name='delete_book'),  # Add this URL pattern to handle form submission in delete_book view.
    path('favorite_book',views.favorite_book, name='favorite_book'),
    path('unfavorite_book',views.unfavorite_book, name='unfavorite_book'),
    # path('info_book',views.info_book, name='info_book'),

   
]
