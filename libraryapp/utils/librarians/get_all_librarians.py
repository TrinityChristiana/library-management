from libraryapp.models import Librarian

def get_all_librarians():
    return Librarian.objects.all()