from libraryapp.models import Book

def get_all_books():
    return Book.objects.all()