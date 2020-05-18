from libraryapp.models import Library

def add_library(form_data):
    new_library = Library.objects.create(
        title = form_data["name"],
        address = form_data["address"]
    )