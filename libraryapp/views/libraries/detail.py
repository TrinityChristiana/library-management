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