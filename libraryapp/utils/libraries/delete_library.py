from ...models import Library

def delete_library(library_id):
    lib = Library.objects.get(pk=library_id)
    lib.delete()