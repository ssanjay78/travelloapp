from django.shortcuts import render, redirect
from .models import PlacesData
from registration.models import Testimonials
from django.contrib.auth.models import User
import json
# Create your views here.

def index(request):
    all_places_data = PlacesData.objects.all()
    user_feedback = Testimonials.objects.all()
    return render(request, 'index.html', {'all_places_data': all_places_data})

def about(request):
    return render(request, 'about.html')