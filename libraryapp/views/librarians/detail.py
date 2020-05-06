import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian, model_factory
from ..connection import Connection
from ...utils import get_librarian

@login_required
def librarian_detail(request, librarian_id):
    if request.method == "GET":
        librarian = get_librarian(librarian_id)
        template = 'librarians/detail.html'
        context = {
            "librarian": librarian
        }

        return render(request, template, context)