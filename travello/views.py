from django.shortcuts import render, redirect
from .models import PlacesData
from .models import Testimonials
from django.contrib.auth.models import User
import json
# Create your views here.

def index(request):
    all_places_data = PlacesData.objects.all()
    user_feedback = Testimonials.objects.all()
    return render(request, 'index.html', {'all_places_data': all_places_data, 'user_feedback':user_feedback})

def testimonials(request):
    if request.method == 'POST':
        username = request.POST['username']
        comments = request.POST['comments']
        
        feedback = Testimonials.objects.create(comment=[comments],name=[username])
        
        return redirect('/')
    else:
        return render(request, 'testimonials.html')