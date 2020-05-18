from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...utils import get_book, get_libraries

@login_required
def book_form(request):
    if request.method == "GET":
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }
        return render(request, template, context)

@login_required
def book_edit_form(request, book_id):
    if request.method == 'GET':
        book = get_book(book_id)
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'book': book,
            'all_libraries': libraries
        }

        return render(request, template, context)