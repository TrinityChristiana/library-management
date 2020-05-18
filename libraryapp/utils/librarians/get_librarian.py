from libraryapp.models import Librarian

def get_librarian(librarian_id):
    return Librarian.objects.get(pk=librarian_id)