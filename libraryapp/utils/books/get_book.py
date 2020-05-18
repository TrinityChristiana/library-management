from libraryapp.models import Book

def get_book(book_id):
    book = Book.objects.get(pk=book_id)
    return book
