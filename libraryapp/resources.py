from tastypie.resources import ModelResource
from libraryapp.models import Librarian, Library, Book

class LibrarianResource(ModelResource):
    class Meta:
        queryset = Librarian.objects.all()
        resource_name = "librarian"

