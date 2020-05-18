import sqlite3
from ...views.connection import Connection
from ...models import Book

def add_book(form_data, request):
    book = Book.objects.create(
        title= form_data['title'], 
        author= form_data['author'], 
        isbn= form_data['isbn'], 
        year_published= form_data['year_published'], 
        location_id= form_data['location'], 
        librarian_id= request.user.id
    )

    # with sqlite3.connect(Connection.db_path) as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     INSERT INTO libraryapp_book(
    #         title, 
    #         author, 
    #         isbn, 
    #         year_published, 
    #         location_id, 
    #         librarian_id
    #     )
    #     Values(?, ?, ?, ?, ?, ?)
    #     """,
    #     (
    #         form_data['title'], 
    #         form_data['author'], 
    #         form_data['isbn'], 
    #         form_data['year_published'], 
    #         request.user.id, 
    #         form_data['location']
    #     ))