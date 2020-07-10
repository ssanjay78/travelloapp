from django.shortcuts import render, redirect
from .models import PlacesData
from django.contrib.auth.models import User
import json
# Create your views here.

def index(request):
    all_places_data = PlacesData.objects.all()
    
    return render(request, 'index.html', {'all_places_data': all_places_data})

