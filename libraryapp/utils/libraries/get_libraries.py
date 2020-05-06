import sqlite3
from libraryapp.models import model_factory, Library
from ...views.connection import Connection
from .create_library import create_library


def get_libraries():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_library()
        db_cursor = conn.cursor()

        db_cursor.execute("""
       SELECT
                    li.id,
                    li.title,
                    li.address,
                    b.id book_id,
                    b.title book_title,
                    b.author,
                    b.year_published,
                    b.isbn
                FROM libraryapp_library li
                JOIN libraryapp_book b ON li.id = b.location_id
        """)

        libraries = db_cursor.fetchall()

        # Start with an empty dictionary
        library_groups = {}

        # Iterate the list of tuples
        for (library, book) in libraries:
            # If the dictionary does have a key of the current
            # library's `id` value, add the key and set the value
            # to the current library
            if library.id not in library_groups:
                # print(library, book)
                library_groups[library.id] = library
                library_groups[library.id].books.append(book)

            # # If the key does exist, just append the current
            # # book to the list of books for the current library
            else:
                library_groups[library.id].books.append(book)


        return library_groups
