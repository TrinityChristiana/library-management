from libraryapp.models import Book

def get_book(book_id):
    book = Book.objects.get(pk=book_id)
    return book
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = create_book()
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         lb.id book_id,
    #         lb.title,
    #         lb.isbn,
    #         lb.author,
    #         lb.year_published,
    #         lb.librarian_id,
    #         lb.location_id,
    #         li.id librarian_id,
    #         u.first_name,
    #         u.last_name,
    #         loc.id library_id,
    #         loc.title library_name
    #     FROM libraryapp_book lb
    #     JOIN libraryapp_librarian li ON lb.librarian_id = li.id
    #     JOIN libraryapp_library loc ON lb.location_id = loc.id
    #     JOIN auth_user u ON u.id = li.user_id
    #     WHERE lb.id = ? 
    #     """
    #     ,
    #     (book_id,)
    #     )
