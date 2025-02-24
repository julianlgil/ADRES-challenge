from django.contrib import admin
from django.urls import path

from csv_validator.views import ValidatorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ValidatorView.as_view(), name='upload_file'),
]

