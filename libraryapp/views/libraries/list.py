from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from ...utils import get_libraries_with_books, add_library

@login_required
def list_libraries(request):
    if request.method == 'GET':
        all_libraries = get_libraries_with_books()
        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }
        
        return render(request, template, context)

    elif request.method == "POST":
        form_data = request.POST
        add_library(form_data)
        return redirect(reverse('libraryapp:libraries'))

