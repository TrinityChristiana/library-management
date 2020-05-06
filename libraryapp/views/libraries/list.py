import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Library
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from ...utils import get_libraries

@login_required
def list_libraries(request):
    if request.method == 'GET':
        all_libraries = get_libraries()
        template = 'libraries/list.html'
        for library in all_libraries:
           print(all_libraries[library].id)
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)
    elif request.method == "POST":
        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO libraryapp_library(
                    title,
                    address
                )
                VALUES(?, ?)
                """, 
                (
                    form_data["name"], 
                    form_data["address"]
                )
            )
            return redirect(reverse('libraryapp:libraries'))

