from django.forms import forms


class UploadJsonFileForm(forms.Form):
    file = forms.FileField()
