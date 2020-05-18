from ...models import Book

def delete_book(book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
