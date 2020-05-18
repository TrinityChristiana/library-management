from libraryapp.models import Librarian

def get_librarian(librarian_id):
    return Librarian.objects.get(pk=librarian_id)
    # with sqlite3.connect(Connection.db_path) as conn:
    #         conn.row_factory = model_factory(Librarian)

    #         db_cursor = conn.cursor()
    #         db_cursor.execute("""
    #             SELECT
    #                 ll.id,
    #                 ll.location_id,
    #                 ll.user_id,
    #                 u.first_name,
    #                 u.last_name  ,
    #                 u.email 
    #             FROM libraryapp_librarian ll
    #             JOIN auth_user u ON 
    #                 u.id = ll.user_id
    #             WHERE ll.id = ?
    #         """, (librarian_id, ))

    #         return db_cursor.fetchone()
