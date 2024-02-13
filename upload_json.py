from django.shortcuts import render, redirect
from .forms import JSONUploadForm
from .models import JSONData
import json

def upload_json(request):
    if request.method == 'POST':
        form = JSONUploadForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = request.FILES['json_file']
            data = json.loads(json_file.read().decode('utf-8'))
            for item in data:
                name = item.get('name', '')[:50]
                date = item.get('date', '')
                if name and date:
                    JSONData.objects.create(name=name, date=date)
            return redirect('view_data')
    else:
        form = JSONUploadForm()
    return render(request, 'upload_json.html', {'form': form})

def view_data(request):
    return render(request, 'view_data.html')