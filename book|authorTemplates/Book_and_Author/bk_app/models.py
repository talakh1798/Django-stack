from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    notes = models.TextField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

def create_book(title,description):
    book = Book.objects.create(title=title, description=description)
    return book

def create_author(first_name, last_name, notes):
    author = Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return author

def get_book(id):
    return Book.objects.get(id=id)

def get_author(id):
    return Author.objects.get(id=id)

def add_book(author,book):
    author.books.add(book)
    return author

def add_author(book, author):
    book.authors.add(author)
    return book
    


