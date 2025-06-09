"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    #auth urls
    #path('login/', CustomLoginView.as_view(), name='login_page'),    # Login page
    path('register/', RegistrationView.as_view(), name='registration_page'),  # Registration page
    #path('profile/', None, name='current_user_profile'),
    path('profile/<str:username>', ProfileDetail.as_view(), name='user_profile'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("privasy/",Privacy.as_view(), name="privacy"),

] 
