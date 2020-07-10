from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('loginwith',views.loginwith,name='loginwith'),
    path('logout',views.logout,name='logout'),
    path('testimonials',views.testimonials,name='testimonials'),
    ]