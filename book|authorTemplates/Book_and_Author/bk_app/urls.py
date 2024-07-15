from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.add_book , name='add_book'),
    path('books/<book_id>', views.book_info , name='book_info'),
    path('add_author', views.add_author, name='add_author'),
    path('author/<author_id>', views.author_info , name='author_info'),



]