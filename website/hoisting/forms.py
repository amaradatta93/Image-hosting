from django import forms


class ImageForm(forms.Form):
    photo = forms.ImageField()
    private = forms.BooleanField(initial=False, required=False)
