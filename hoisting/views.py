from PIL import Image as PIL
from django.core.files.images import get_image_dimensions
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .forms import ImageForm
from .models import Image


def save_image(request):
    saved = False
    image = None
    if request.method == "POST":
        image_form = ImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            image = Image()
            image.photo = image_form.cleaned_data["photo"]
            width, height = get_image_dimensions(image.photo)
            image.width = width
            image.length = height
            image.private = image_form.cleaned_data['private'] or False
            image.save()
            saved = True

    return render(request, 'saved.html', {'saved': saved, 'id': image.pk if image else None})


def get_image_by_resolution(request, width, height):
    """
    Find all the images in the database with this width x height and choose one of those images, and render that image
    """
    image = Image.objects.filter(width=width, length=height).order_by('uploaded_at').first()
    if not image:
        image = Image.objects.all().extra(select={'pixels': 'abs(width - %s) * abs(length - %s)'},
                                          select_params=(int(width), int(height))).order_by('pixels').first()
        if not image:
            raise Http404()
        else:
            resized = PIL.open(image.photo).resize((int(width), int(height)), PIL.LANCZOS)
            response = HttpResponse(content_type="image/png")
            resized.save(response, "PNG")
            return response
    else:
        return HttpResponse(image.photo, content_type='image/jpeg')


def get_image_by_id(request, id):
    """
    Find an image with this ID in the database and return the image, otherwise 404
    :return:
    """
    image = get_object_or_404(Image, pk=id)
    return HttpResponse(image.photo, content_type='image/jpeg')
