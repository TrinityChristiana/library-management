from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ...utils import get_book, delete_book, update_book

@login_required
def book_details(request, book_id):
    if request.method == "GET":
        book = get_book(book_id)
        template = 'books/detail.html'
        context = {
            'book': book
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            delete_book(book_id)
            return redirect(reverse('libraryapp:books'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            update_book(form_data, book_id)
            return redirect(reverse('libraryapp:books'))
