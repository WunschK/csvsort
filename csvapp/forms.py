from django import forms
from .models import UploadedFile

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
    column_name = forms.CharField(max_length=255)