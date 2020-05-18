from ...models import Library

def update_library(form_data, library_id):
    lib = Library.objects.get(pk=library_id)
    lib.title = form_data["name"]
    lib.address = form_data["address"]
    lib.save()