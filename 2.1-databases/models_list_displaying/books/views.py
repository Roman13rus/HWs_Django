from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    # books_obj = Book.objects.all()
    # context = {'books': books_obj}
    context = {}
    return render(request, template, context)
def books_list(request):
    template = 'books/books_list.html'
    # books_obj = Book.objects.all()
    # context = {'books': books_obj}
    context = {}
    return render(request, template, context)