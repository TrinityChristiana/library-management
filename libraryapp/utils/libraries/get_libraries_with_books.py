from libraryapp.models import Library, Book

def get_libraries_with_books():
    libraries = Library.objects.all()
    books = Book.objects.all()
    library_groups = {}

    for library in libraries:
        library_groups[library.id] = {
            "library": library,
            "books": []
        }

    for book in books:
        if book.location_id in library_groups:
            library_groups[book.location_id]["books"].append(book)

    return library_groups