from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...utils import get_all_librarians


@login_required
def list_librarians(request):
    if request.method == 'GET':
        all_librarians = get_all_librarians()
        template_name = 'librarians/list.html'
        context = {
            'all_librarians': all_librarians
        }

        return render(request, template_name, context)