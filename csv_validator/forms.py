from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Selecciona un archivo CSV o TXT")