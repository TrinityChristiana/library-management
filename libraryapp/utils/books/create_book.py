import sqlite3
from libraryapp.models import Book, model_factory, Librarian, Library
from ...views.connection import Connection


def create_book():
    def create(cursor, row):
        _row = sqlite3.Row(cursor, row)

        book = Book()
        book.id = _row["book_id"]
        book.author = _row["author"]
        book.isbn = _row["isbn"]
        book.title = _row["title"]
        book.year_published = _row["year_published"]

        librarian = Librarian()
        librarian.id = _row["librarian_id"]
        librarian.first_name = _row["first_name"]
        librarian.last_name = _row["last_name"]

        library = Library()
        library.id = _row["library_id"]
        library.title = _row["library_name"]

        book.librarian = librarian
        book.location = library

        return book
    return create
    
    