from django.shortcuts import render
from django.http import HttpResponse
from .forms import CSVUploadForm
import os
from .sort_csv import sort_csv

def index(request):
    pass

def sort_csv_view(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file
            uploaded_file = request.FILES['csv_file']
            # Define the path for the uploaded file
            upload_dir = 'media/uploads'
            file_path = os.path.join(upload_dir, uploaded_file.name)
            # Save the uploaded file to the defined path
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Sort the uploaded CSV file
            sorted_file_path = os.path.join(upload_dir, 'sorted_persons.csv')
            sort_csv(file_path, sorted_file_path, form.cleaned_data['column_name'])

            # Serve the sorted CSV file as a download
            with open(sorted_file_path, 'rb') as sorted_file:
                response = HttpResponse(sorted_file.read(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename=sorted_persons.csv'
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'sort_csv.html', {'form': form})