import sqlite3
from ...views.connection import Connection
from libraryapp.models import Library, model_factory

def get_library(library_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            ll.id,
            ll.title,
            ll.address
        FROM libraryapp_library ll
        WHERE ll.id == ?
        """, (library_id, ))

        return db_cursor.fetchone()