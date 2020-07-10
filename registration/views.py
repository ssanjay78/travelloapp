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
        # print(User.is_authenicated, User.first_name)

        if user is not None:
            print("Logged in as : ", user.is_authenticated, user.first_name)
            return redirect('/')
        else:
            messages.info(request,"Credential does not exist!")
            return redirect('loginwith')
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
    user_feedback = Testimonials.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        comments = request.POST['comments']
        
        feedback = Testimonials.objects.create(comment=[comments],name=[username])
        
        return render(request, 'index.html', {'user_feedback': user_feedback})
    else:
        return render(request, 'testimonials.html')