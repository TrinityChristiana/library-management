from ...models import Library

def update_library(form_data, library_id):
    lib = Library.objects.get(pk=library_id)
    lib.title = form_data["name"]
    lib.address = form_data["address"]
    lib.save()

    # with sqlite3.connect(Connection.db_path) as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     UPDATE libraryapp_library
    #     SET title = ?,
    #         address = ?
    #     WHERE id = ?; 
    #     """, (
    #         form_data["name"],
    #         form_data["address"],
    #         library_id
    #     ))
