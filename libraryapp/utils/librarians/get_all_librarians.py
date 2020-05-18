from libraryapp.models import Librarian



def get_all_librarians():
    return Librarian.objects.all()
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Library)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     select
    #         l.id,
    #         l.location_id,
    #         l.user_id,
    #         u.first_name,
    #         u.last_name,
    #         u.email
    #     from libraryapp_librarian l
    #     join auth_user u on l.user_id = u.id
    #     """)

    #     return db_cursor.fetchall()