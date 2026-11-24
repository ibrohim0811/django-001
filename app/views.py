from django.shortcuts import get_object_or_404, redirect, render
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'main.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'detail.html', {'book': book})


