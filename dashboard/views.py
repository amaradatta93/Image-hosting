from django.db.models import Count
from django.shortcuts import render

from hoisting.models import Image


def dashboard(request):
    """
    Gets the latest images that are NOT private
    and displays in a template for the home page.
    Also has a button to take you to the "add" page
    """
    sort = request.GET.get("sort", "total_vote")
    sort = "-" + (sort if sort in ['total_vote', 'uploaded_at'] else "total_vote")
    images = Image.objects.filter(private=False).annotate(total_vote=Count("vote")).order_by(sort)[:50]
    return render(request, 'dashboard.html', {'images': images})
