from libraryapp.models import Library, Book

def get_libraries():
    return Library.objects.all()