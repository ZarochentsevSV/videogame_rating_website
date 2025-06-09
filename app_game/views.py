
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

class ExtraContext(object):
    extra_context = {}
    _object_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        context.update(self._object_context)
        return context


class GameBase(ExtraContext):
    model = Game
    #form_class = GenreForm
    _object_context = {'object_type': 'genre'}

class GameListView(GameBase, ListView):
    template_name = 'game/game_list.html'
    context_object_name='games'

class GameDetailView(GameBase, TemplateView):
    '''CBV return game page'''
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

class GameCreateView(GameBase, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = GameForm
    template_name = 'game/game_form.html'
    success_url = reverse_lazy('game_list')

class GameUpdateView(GameBase, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = GameForm
    template_name = 'game/game_form.html'
    success_url = reverse_lazy('game_list')

class GameDeleteView(GameBase, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    template_name = 'game/game_confirm_delete.html'
    success_url = reverse_lazy('game_list')


#------genres views--------


class GenreBase(ExtraContext):
    model = Genre
    #form_class = GenreForm
    _object_context = {'object_type': 'genre'}

class GenreListView(GenreBase, ListView):
    template_name = 'unified_templates/unified_list.html'
    context_object_name='genres'

class GenreDetailView(GenreBase, DetailView):
    model = Genre
    template_name = 'genre/genre_detail.html'

class GenreCreateView(GenreBase, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = GenreForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('genre_list')

class GenreUpdateView(GenreBase, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = GenreForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('genre_list')

class GenreDeleteView(GenreBase, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    template_name = 'unified_templates/unified_confirm_delete.html'
    success_url = reverse_lazy('genre_list')

#----------Developer Views----------

class DeveloperBase(ExtraContext):
    model = Developer
    #form_class = DeveloperForm
    _object_context = {'object_type': 'developer'}
    
class DeveloperListView(DeveloperBase, ListView):
    template_name = 'unified_templates/unified_list.html'
    context_object_name='developers'

class DeveloperDetailView(DeveloperBase, DetailView):
    template_name = 'unified_templates/unified_detail.html'

class DeveloperCreateView(DeveloperBase, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = DeveloperForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('developer_list')

class DeveloperUpdateView(DeveloperBase, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = DeveloperForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('developer_list')

class DeveloperDeleteView(DeveloperBase, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    template_name = 'unified_templates/unified_confirm_delete.html'
    success_url = reverse_lazy('developer_list')

#-----------Publisher Views------------

class PublisherBase(ExtraContext):
    model = Publisher
    #form_class = PublisherForm
    _object_context = {'object_type': 'publisher'}

class PublisherListView(PublisherBase, ListView):
    template_name = 'unified_templates/unified_list.html'

class PublisherDetailView(PublisherBase, DetailView):
    model = Publisher
    template_name = 'publisher/publisher_detail.html'

class PublisherCreateView(PublisherBase, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = PublisherForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherUpdateView(PublisherBase, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = PublisherForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('publisher_list')

class PublisherDeleteView(PublisherBase, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    template_name = 'unified_templates/unified_confirm_delete.html'
    success_url = reverse_lazy('publisher_list')

#---------Platform Views----------

class PlatformBase(ExtraContext):
    model = Platform
    #form_class = PlatformForm
    _object_context = {'object_type': 'platform'}

class PlatformListView(PlatformBase, ListView):
    template_name = 'unified_templates/unified_list.html'
    context_object_name='platforms'

class PlatformDetailView(PlatformBase, DetailView):
    template_name = 'unified_templates/unified_detail.html'

class PlatformCreateView(PlatformBase, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = PlatformForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('platform_list')

class PlatformUpdateView(PlatformBase, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    form_class = PlatformForm
    template_name = 'unified_templates/unified_form.html'
    success_url = reverse_lazy('platform_list')

class PlatformDeleteView(PlatformBase, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    template_name = 'unified_templates/unified_confirm_delete.html'
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

