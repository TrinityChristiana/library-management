import sqlite3
from libraryapp.models import Book, model_factory
from ...views.connection import Connection

def get_book(book_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Book)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                lb.id,
                lb.title,
                lb.author,
                lb.year_published,
                lb.isbn,
                lb.location_id,
                lb.librarian_id
            FROM libraryapp_book lb
            WHERE lb.id = ? 
        """,
        (book_id,)
        )

        return db_cursor.fetchone()