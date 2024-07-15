from django.shortcuts import render, redirect
from.models import Book , Author
from . import models

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        book = models.create_book(title, description)
        return redirect('add_book')
    else:
        books = Book.objects.all()
        return render(request, 'book.html', {'books': books})

def book_info(request, book_id):
    book = models.get_book(book_id)
    if request.method == 'POST':
        author_id = request.POST['author']
        author = models.get_author(author_id)
        models.add_book(author, book)
        return redirect('book_info', book_id=book_id)
    authors = Author.objects.all()
    return render(request, 'book_info.html', {'book': book, 'authors': authors})

def add_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        author = models.create_author(first_name, last_name, notes)
        return redirect('add_author')
    else:
        authors = Author.objects.all()
        return render(request, 'author.html', {'authors': authors})
    

def author_info(request, author_id):
    author = models.get_author(author_id)
    if request.method == 'POST':
        book_id = request.POST['book']
        book = models.get_book(book_id)
        models.add_author(book, author)
        return redirect('author_info', author_id=author_id)
    books = Book.objects.all()
    return render(request, 'author_info.html', {'author': author, 'books': books})