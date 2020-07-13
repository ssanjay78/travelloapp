from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonials
from django.contrib.auth.models import User,auth

# Create your views here.

def loginwith(request):
    if request.method == 'POST':
        messages.info(request,'')
        username = request.POST["username"]
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        try:    
            auth.login(request, user)
        except Exception:
            messages.info(request,"Credential does not exist!")
            return redirect('loginwith')
        return redirect('/')
    else:
        return render(request,'loginwith.html')

def register(request):
    messages.info(request,'')
    if request.method == 'POST':
        # Get the data from Registration page
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Verify if there is existing user
        if User.objects.filter(username=username).exists():
            messages.info(request, "This user is already registered.")
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request,"This email is already in use.")
            return redirect('register')
        else:
            if password1 == password2:
                # Create a user with this data
                user = User.objects.create_user(username, email=email, password=password1, first_name=first_name, last_name=last_name)
                # Save this user in the database
                user.save()
                return redirect('loginwith')
            else:
                messages.info(request,"Password not matching.")
                return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def testimonials(request):
    slang_words = ['fuck ', 'sex ', 'chutiya ', 'bc ', 'mc ', 'gandu ', 'benchod ']
    if request.method == 'POST':
        name = request.user.first_name
        comments = request.POST['comments']

        for each in slang_words:
            if each in comments.lower():
                return redirect('/')

        feedback = Testimonials.objects.create(comment=comments,name=name)
        feedback.save()

        return redirect('/')
    else:
        return render(request, 'testimonials.html')