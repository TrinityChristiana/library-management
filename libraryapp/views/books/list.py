import sqlite3
from django.shortcuts import render, redirect, reverse 
from libraryapp.models import Book, model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from ...utils import get_all_books, add_book



@login_required
def book_list(request):
    if request.method == 'GET':
        all_books = get_all_books()
        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    elif request.method == "POST":
        form_data = request.POST
        add_book(form_data, request) 
        return redirect(reverse('libraryapp:books'))
