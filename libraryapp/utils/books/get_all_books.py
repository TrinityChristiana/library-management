import sqlite3
from libraryapp.models import Book, model_factory
from ...views.connection import Connection

def get_all_books():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Book)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            b.id,
            b.title,
            b.isbn,
            b.author,
            b.year_published,
            b.librarian_id,
            b.location_id
        from libraryapp_book b
        """)

        return db_cursor.fetchall()