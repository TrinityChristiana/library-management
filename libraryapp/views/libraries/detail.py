import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library, model_factory
from ..connection import Connection

def get_library(library_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            ll.id,
            ll.title,
            ll.address
        FROM libraryapp_library ll
        WHERE ll.id == ?
        """, (library_id, ))

        return db_cursor.fetchone()


@login_required
def library_detail(request, library_id):
    if request.method == "GET":
       library = get_library(library_id)

       template = "libraries/detail.html"
       context = {
           'library': library
       }

       return render(request, template, context)