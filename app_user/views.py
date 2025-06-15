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
from app_user.util import IsInStaffCheckMixin, IsUserAllowedCheckMixin
from app_game.models import Review
from .models import *
from .forms import *
import logging

class RegistrationView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    authentication_form = LogInForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home') 

class ProfileDetail(IsUserAllowedCheckMixin, View):
    
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
