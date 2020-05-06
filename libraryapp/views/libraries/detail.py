import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library, model_factory
from ..connection import Connection
from ...utils import get_library


@login_required
def library_detail(request, library_id):
    if request.method == "GET":
        library = get_library(library_id)
        template = "libraries/detail.html"
        context = {
            'library': library
        }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST
            
        if "actual_method" in form_data and form_data["actual_method"] == "Delete":
            print("DELETING ************")
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE from libraryapp_library
                WHERE id = ?
                """, (library_id, ))

            return redirect(reverse("libraryapp:libraries"))

        if "actual_method" in form_data and form_data['actual_method'] == "PUT":
            print("UPDATING ************")
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE libraryapp_library
                SET title = ?,
                    address = ?
                WHERE id = ?; 
                """, (
                    form_data["name"],
                    form_data["address"],
                    library_id
                ))
            return redirect(reverse("libraryapp:libraries"))
