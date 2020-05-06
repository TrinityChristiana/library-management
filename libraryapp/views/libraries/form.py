import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, model_factory
from ..connection import Connection
from ...utils import get_library

@login_required
def library_form(request):
    if request.method == "GET":
        template = "libraries/form.html"
        context = {}
        return render(request, template, context)

@login_required
def library_edit_form(request, library_id):
    # print(request.method, "***********")
    if request.method == "GET":
        library = get_library(library_id)
        template = "libraries/form.html"
        context = {'library': library}
        return render(request, template, context)
