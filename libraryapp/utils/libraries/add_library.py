from libraryapp.models import Library

def add_library(form_data):
    new_library = Library.objects.create(
        title = form_data["name"],
        address = form_data["address"]
    )

    # with sqlite3.connect(Connection.db_path) as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #         INSERT INTO libraryapp_library(
    #             title,
    #             address
    #         )
    #         VALUES(?, ?)
    #         """, 
    #         (
    #             form_data["name"], 
    #             form_data["address"]
    #         )
    #     )