from ...models import Book

def add_book(form_data, request):
    book = Book.objects.create(
        title= form_data['title'], 
        author= form_data['author'], 
        isbn= form_data['isbn'], 
        year_published= form_data['year_published'], 
        location_id= form_data['location'], 
        librarian_id= request.user.id
    )