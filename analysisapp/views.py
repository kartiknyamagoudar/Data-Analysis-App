from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DataEntry

def home(request):
    data_entries = DataEntry.objects.all()
    return render(request, 'analysisapp/home.html', {'data_entries': data_entries})
