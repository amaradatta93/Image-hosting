from django.http import Http404
from django.shortcuts import render
from hoisting.models import Image


def dashboard(request):
    """
    Gets the latest images that are NOT private
    and displays in a template for the home page.
    Also has a button to take you to the "add" page
    """
    images = Image.objects.filter(private=False).order_by('-uploaded_at')[:50]

    if not images:
        raise Http404()

    return render(request, 'dashboard.html', {'images': images})
