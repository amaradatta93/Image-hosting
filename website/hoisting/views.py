from django.core.files.images import get_image_dimensions
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ImageForm
from .models import Image
from logging import getLogger

logger = getLogger(__name__)


def save_image(request):
    saved = False
    image = None
    if request.method == "POST":
        # Get the posted form
        image_form = ImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            # logger.info("Validated form")
            print "Validated form"
            image = Image()
            image.photo = image_form.cleaned_data["photo"]
            width, height = get_image_dimensions(image.photo)
            image.width = width
            image.length = height
            image.private = image_form.cleaned_data['private']
            image.save()
            logger.info("Saved image")
            saved = True
        else:
            logger.error("Unable to valid form")

    return render(request, 'saved.html', {'saved': saved, 'id': image.pk if image else None})


def get_image_by_resolution(request, width, height):
    """
    Find all the images in the database with this width x height and choose one of those images, and render that image
    """
    image = Image.objects.filter(width=width, height=height).first()

    # if image exists, render template with the image. otherwise, 404
    pass


def get_image_by_id(request, id):
    """
    Find an image with this ID in the database and return the image, otherwise 404
    :return:
    """
    image = get_object_or_404(Image, pk=id)
    return HttpResponse(image.photo, content_type='image/jpeg')
