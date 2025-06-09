
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
import random as rand
from .models import *
from .forms import *
import logging

logger = logging.getLogger(__name__)
# Create your views here.

class Home(View):
    def get(self, request):
        context = {}
        return render(request,  'home/index.html', context)


class GameBaseView(View):
    model = Game
    fields = '__all__'
    success_url = reverse_lazy('Game:all')

class GameListView(ListView):
    model = Game
    template_name = 'game/game_list.html'
    context_object_name='games'

class GameDetailView(TemplateView):
    '''CBV return game page'''
    model = Game
    template_name = 'game/game_detail.html'
    def get(self, request, pk, *args, **kwargs):
        game = get_object_or_404(Game, id=pk)
        if game:
            context = {}
            if self.request.user.is_authenticated:
                user_id = self.request.user.id
                # user_review = Review.objects.filter(game=pk, user=user_id).first()
                # context['current_user_review'] = user_review if user_review else None
            else:
                context['current_user_review'] = None
            context['game'] = game
            context['reviews'] = Review.objects.filter(game=pk)
            return render(request, self.template_name, context)
        return reverse_lazy('game_list')

class GameSearchView(View):
    '''This CBV finds game data by title, release date, publisher, developer, platform, genre
    
    Return filtered game list'''
    template = 'game/search.html'
    def get(self, request, *args, **kwargs):
        context = {}


        return render(request, self.template, context)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pk = self.kwargs['pk']
    #     context['game'] = get_object_or_404(Game, id=pk)
    #     context['reviews'] = Review.objects.filter(game=pk)
    #     context['current_user_review'] = Review.objects.filter(game=pk, user=get_user_model())
    #     return context

class GameCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Game
    form_class = GameForm
    template_name = 'game/game_form.html'
    success_url = reverse_lazy('game_list')

class GameUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Game
    form_class = GameForm
    template_name = 'game/game_form.html'
    success_url = reverse_lazy('game_list')

class GameDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Game
    form_class = GameForm
    template_name = 'game/game_confirm_delete.html'
    success_url = reverse_lazy('game_list')


#------genres views--------

class GenreBaseView(View):
    model = Genre
    form_class = GenreForm
    fields = '__all__'
    success_url = reverse_lazy('genres:all')

class GenreListView(ListView):
    model = Genre
    template_name = 'genre/genre_list.html'
    context_object_name='genres'

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre/genre_detail.html'

class GenreCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Genre
    form_class = GenreForm
    template_name = 'genre/genre_form.html'
    success_url = reverse_lazy('genre_list')

class GenreUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Genre
    form_class = GenreForm
    template_name = 'genre/genre_form.html'
    success_url = reverse_lazy('genre_list')

class GenreDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Genre
    template_name = 'genre/genre_confirm_delete.html'
    success_url = reverse_lazy('genre_list')

#----------Developer Views----------

class DeveloperBaseView(View):
    model = Developer
    form_class = DeveloperForm
    fields = '__all__'
    success_url = reverse_lazy('developers:all')

class DeveloperListView(ListView):
    model = Developer
    template_name = 'developer/developer_list.html'
    context_object_name='developers'

class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'developer/developer_detail.html'

class DeveloperCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Developer
    form_class = DeveloperForm
    template_name = 'developer/developer_form.html'
    success_url = reverse_lazy('developer_list')

class DeveloperUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Developer
    form_class = DeveloperForm
    template_name = 'developer/developer_form.html'
    success_url = reverse_lazy('developer_list')

class DeveloperDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Developer
    template_name = 'developer/developer_confirm_delete.html'
    success_url = reverse_lazy('developer_list')

#-----------Publisher Views------------

class PublisherBaseView(View):
    model = Publisher
    form_class = PublisherForm
    fields = '__all__'
    success_url = reverse_lazy('publishers:all')

class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher/publisher_list.html'
    context_object_name='publishers'

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'publisher/publisher_detail.html'

class PublisherCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/publisher_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/publisher_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Publisher
    template_name = 'publisher/publisher_confirm_delete.html'
    success_url = reverse_lazy('publisher_list')

#---------Platform Views----------

class PlatformBaseView(View):
    model = Platform
    form_class = PlatformForm
    fields = '__all__'
    success_url = reverse_lazy('platforms:all')

class PlatformListView(ListView):
    model = Platform
    template_name = 'platform/platform_list.html'
    context_object_name='platforms'

class PlatformDetailView(DetailView):
    model = Platform
    template_name = 'platform/platform_detail.html'

class PlatformCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Platform
    form_class = PlatformForm
    template_name = 'platform/platform_form.html'
    success_url = reverse_lazy('platform_list')

class PlatformUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Platform
    form_class = PlatformForm
    template_name = 'platform/platform_form.html'
    success_url = reverse_lazy('platform_list')

class PlatformDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Platform
    template_name = 'platform/platform_confirm_delete.html'
    success_url = reverse_lazy('platform_list')


#----------Reveiw views--------------


class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name='reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'

class ReviewCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')

