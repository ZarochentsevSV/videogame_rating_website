"""
URL configuration for server project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    #games urls
    path('games/', GameListView.as_view(), name='game_list'),
    path('games/create', GameCreateView.as_view(), name='game_create'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('games/<int:pk>/update/', GameUpdateView.as_view(), name='game_update'),
    path('games/<int:pk>/delete/', GameDeleteView.as_view(), name='game_delete'),
    path('games/search', GameSearchView.as_view(), name='game_search'),

    #genre urls
    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('genres/create', GenreCreateView.as_view(), name="genre_create"),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('genres/<int:pk>/update/', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),
    
    #developers urls
    path('developers/', DeveloperListView.as_view(), name='developer_list'),
    path('developers/create', DeveloperCreateView.as_view(), name="developer_create"),
    path('developers/<int:pk>/', DeveloperDetailView.as_view(), name='developer_detail'),
    path('developers/<int:pk>/update/', DeveloperUpdateView.as_view(), name='developer_update'),
    path('developers/<int:pk>/delete/', DeveloperDeleteView.as_view(), name='developer_delete'),

    #platforms urls
    path('platform/', PlatformListView.as_view(), name='platform_list'),
    path('platform/create', PlatformCreateView.as_view(), name="platform_create"),
    path('platform/<int:pk>/', PlatformDetailView.as_view(), name='platform_detail'),
    path('platform/<int:pk>/update/', PlatformUpdateView.as_view(), name='platform_update'),
    path('platform/<int:pk>/delete/', PlatformDeleteView.as_view(), name='platform_delete'),

    #publishers urls
    path('publisher/', PublisherListView.as_view(), name='publisher_list'),
    path('publisher/create', PublisherCreateView.as_view(), name="publisher_create"),
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publisher/<int:pk>/update/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher/<int:pk>/delete/', PublisherDeleteView.as_view(), name='publisher_delete'),

    #other urls

] 