from ...models import Book
def delete_book(book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    # with sqlite3.connect(Connection.db_path) as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     DELETE FROM libraryapp_book
    #     WHERE id = ?
    #     """, (book_id,))
