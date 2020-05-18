from libraryapp.models import Library

def get_library(library_id):
    return Library.objects.get(pk=library_id)