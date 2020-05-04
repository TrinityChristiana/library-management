import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian, model_factory
from ..connection import Connection

def get_librarian(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Librarian)

            db_cursor = conn.cursor()
            db_cursor.execute("""
                SELECT
                    ll.id,
                    ll.location_id,
                    ll.user_id,
                    u.first_name,
                    u.last_name  ,
                    u.email 
                FROM libraryapp_librarian ll
                JOIN auth_user u ON 
                    u.id = ll.user_id
                WHERE ll.id = ?
            """, (librarian_id, ))

            return db_cursor.fetchone()

@login_required
def librarian_detail(request, librarian_id):
    if request.method == "GET":
            librarian = get_librarian(librarian_id)
            template = 'librarians/detail.html'
            context = {
                "librarian": librarian
            }

            return render(request, template, context)