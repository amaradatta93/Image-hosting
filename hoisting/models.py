from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField()
    length = models.IntegerField()
    private = models.BooleanField(default=False)


class Vote(models.Model):
    image_vote = models.ForeignKey(Image, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(null=False)

    class Meta:
        unique_together = ('image_vote', 'ip')
