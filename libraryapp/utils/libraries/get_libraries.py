from libraryapp.models import Library, Book

def get_libraries():
    return Library.objects.all()

    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Library)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         *
    #     FROM libraryapp_library li
    #     """)

    

    # conn.row_factory = model_factory(Book)
    # db_cursor = conn.cursor()

    # db_cursor.execute("""
    # SELECT
    #     *
    # FROM libraryapp_book
    # """)
