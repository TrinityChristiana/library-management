from ...models import Book
def update_book(form_data, book_id):
    book = Book.objects.get(pk=book_id)
    book.title= form_data['title']
    book.author= form_data['author'] 
    book.isbn= form_data['isbn']
    book.year_published= form_data['year_published']
    book.location_id= form_data['location']
    book.save()

    # with sqlite3.connect(Connection.db_path) as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     UPDATE libraryapp_book
    #     SET title = ?,
    #         author = ?,
    #         isbn = ?,
    #         year_published = ?,
    #         location_id = ?
    #     WHERE id = ?
    #     """,
    #     (
    #         form_data['title'], form_data['author'],
    #         form_data['isbn'], form_data['year_published'],
    #         form_data["location"], book_id,
    #     ))
