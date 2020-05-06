import sqlite3
from libraryapp.models import model_factory, Library, Book
from ...views.connection import Connection

def create_library():
    def create(cursor, row):
        _row = sqlite3.Row(cursor, row)

        library = Library()
        library.id = _row["id"]
        library.title = _row["title"]
        library.address = _row["address"]

        # Note: You are adding a blank books list to the library object
        # This list will be populated later (see below)
        library.books = []

        book = Book()
        book.id = _row["book_id"]
        book.title = _row["book_title"]
        book.author = _row["author"]
        book.isbn = _row["isbn"]
        book.year_published = _row["year_published"]

        # Return a tuple containing the library and the
        # book built from the data in the current row of
        # the data set
        return (library, book,)
    return create