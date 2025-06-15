# Import necessary modules and models
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from app_game.models import Review
from .models import *
from .forms import *
import logging

class RegistrationView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login_page')
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    authentication_form = LogInForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home') 

class ProfileDetail(UserPassesTestMixin, View):
    
    def get(self, request, username, *args, **kwargs):
        template = 'user/page.html'
        user = User.objects.filter(username = username).first()
        reviews = Review.objects.filter(user__id = user.id)
        context = {
            'user': user,
            'reviews': reviews,
            }
        return render(request, template, context)

class Privacy(View):
    def get(self, request, *args, **kwargs):
        template = 'user/privacy.html'
        context = {}
        return render(request, template, context)
# # Define a view function for the login page
# class LoginView(View):
#     def get(self, request):
#         return render(request, 'auth/login.html')
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Check if a user with the provided username exists
#         if not Profile.objects.user.filter(username=username).exists():
#             # Display an error message if the username does not exist
#             messages.error(request, 'Invalid Username')
#             return HttpResponseRedirect(reverse_lazy('login_page'))
        
#         # Authenticate the user with the provided username and password
#         user = authenticate(username=username, password=password)
        
#         if user is None:
#             # Display an error message if authentication fails (invalid password)
#             messages.error(request, "Invalid Password")
#             return HttpResponseRedirect(reverse_lazy('login_page'))
#         else:
#             # Log in the user and redirect to the home page upon successful login
#             login(request, user)
#             return HttpResponseRedirect(reverse_lazy('home'))

# class RegistrationView(View):
#     def get(self, request):
#         return render(request, 'auth/register.html')

#     def post(self, request):
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         birthday = request.POST.get('birthday')
        
#         # Check if a user with the provided username or email already exists
#         if Profile.objects.user.filter(username=username).exists():
#             # Display an information message if the username is taken
#             messages.info(request, "Username already taken!")
#             return redirect('/register/')
#         if Profile.objects.user.filter(email=email).exists():
#             messages.info(request, "Email already taken!")
#             return redirect('/register/')
        
#         # Create a new User object with the provided information
#         user = Profile.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email = email,
#             birthday = birthday
#         )
        
#         # Set the user's password and save the user object
#         user.set_password(password)
#         user.save()
        
#         # Display an information message indicating successful account creation
#         messages.info(request, "Account created Successfully!")
#         return HttpResponseRedirect(reverse_lazy('home'))


# def login_page(request):
#     # Check if the HTTP request method is POST (form submission)
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Check if a user with the provided username exists
#         if not User.objects.filter(username=username).exists():
#             # Display an error message if the username does not exist
#             messages.error(request, 'Invalid Username')
#             return redirect('/login/')
        
#         # Authenticate the user with the provided username and password
#         user = authenticate(username=username, password=password)
        
#         if user is None:
#             # Display an error message if authentication fails (invalid password)
#             messages.error(request, "Invalid Password")
#             return redirect('/login/')
#         else:
#             # Log in the user and redirect to the home page upon successful login
#             login(request, user)
#             return redirect('/home/')
    
#     # Render the login page template (GET request)
#     return render(request, 'auth/login.html')

# # Define a view function for the registration page
# def register_page(request):
#     # Check if the HTTP request method is POST (form submission)
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         birthday = request.POST.get('birthday')
        
#         # Check if a user with the provided username or email already exists
#         if User.objects.filter(username=username).exists():
#             # Display an information message if the username is taken
#             messages.info(request, "Username already taken!")
#             return redirect('/register/')
#         if User.objects.filter(email=email).exists():
#             messages.info(request, "Email already taken!")
#             return redirect('/register/')
        
#         # Create a new User object with the provided information
#         user = User.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             username=username
#         )
        
#         # Set the user's password and save the user object
#         user.set_password(password)
#         user.save()
        
#         # Display an information message indicating successful account creation
#         messages.info(request, "Account created Successfully!")
#         return redirect('/register/')
    
#     # Render the registration page template (GET request)
#     return render(request, 'auth/register.html')
