from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ...utils import get_library, update_library


@login_required
def library_detail(request, library_id):
    if request.method == "GET":
        library = get_library(library_id)
        template = "libraries/detail.html"
        context = {
            'library': library
        }

        return render(request, template, context)

    if request.method == "POST":
        form_data = request.POST

        if "actual_method" in form_data and form_data['actual_method'] == "PUT":
            update_library(form_data, library_id)
           
            return redirect(reverse("libraryapp:libraries"))
