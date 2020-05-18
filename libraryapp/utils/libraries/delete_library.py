from ...models import Library
def delete_library(library_id):
    lib = Library.objects.get(pk=library_id)
    lib.delete()
    # with sqlite3.connect(Connection.db_path) as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     DELETE from libraryapp_library
    #     WHERE id = ?
    #     """, (library_id, ))