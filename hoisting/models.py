from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField()
    length = models.IntegerField()
    private = models.BooleanField(default=False)
