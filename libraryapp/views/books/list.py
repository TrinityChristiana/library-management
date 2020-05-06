import sqlite3
from django.shortcuts import render, redirect, reverse 
from libraryapp.models import Book, model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from ...utils import get_all_books



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

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book(
                title, 
                author, 
                isbn, 
                year_published, 
                location_id, 
                librarian_id
            )
            Values(?, ?, ?, ?, ?, ?)
            """,
            (
                form_data['title'], 
                form_data['author'], 
                form_data['isbn'], 
                form_data['year_published'], 
                request.user.librarian.id, 
                form_data['location']
            ))

        return redirect(reverse('libraryapp:books'))
