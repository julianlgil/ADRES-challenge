from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import UploadFileForm
from .validators import Validator

class ValidatorView(View):

    def get(self, request):
        form = UploadFileForm()
        return render(request, 'upload_file.html', {"form": form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']

            if not file.name.endswith('.csv') and not file.name.endswith('.txt'):
                messages.error(request, "El archivo debe tener extensión .csv o .txt.")
            else:
                errors = Validator.validate(file)
                if errors:
                    for error in errors:
                        messages.error(request, error)
                    messages.error(request, "Se encontraron errores.")
                else:
                    messages.success(request, "¡Archivo validado exitosamente!")

            return redirect(reverse('upload_file'))



