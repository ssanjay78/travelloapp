from django.shortcuts import render, redirect
from .models import PlacesData
from .models import Testimonials
from django.contrib.auth.models import User
import json
# Create your views here.
global all_places_data
all_places_data = PlacesData.objects.all()

def index(request):

    user_feedback = Testimonials.objects.all()
    return render(request, 'index.html', {'all_places_data': all_places_data, 'user_feedback':user_feedback})

def testimonials(request):
    if request.method == 'POST':
        username = request.POST['username']
        comments = request.POST['comments']
        relation = request.POST['relation']
        if relation=='no':
            relation='Employee'
        else:
            relation='Customer'
        all_places_data.comment = comments
        all_places_data.name = username
        all_places_data.save()
        
        return redirect('/')
    else:
        return render(request, 'testimonials.html')