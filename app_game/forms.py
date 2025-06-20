from django import forms
from .models import *
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import ModelMultipleChoiceField

class CustomSelectMultiple(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s" %(obj.name)

class GameForm(forms.ModelForm):
    #genres = forms.ModelChoiceField(queryset=Genre.objects.all(), required=True, to_field_name="name")
    age_options = (
        ('0','0+'),
        ('3','3+'),
        ('6','6+'),
        ('12','12+'),
        ('16','16+'),
        ('18','18+')
    )
    age_rating = forms.ChoiceField(choices=age_options)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    genres = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=Genre.objects.all())
    platforms = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=Platform.objects.all())
    publishers = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=Publisher.objects.all())
    developers  = CustomSelectMultiple(widget=forms.CheckboxSelectMultiple, queryset=Developer.objects.all())
    release_date =  forms.DateField(widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),input_formats=["%Y-%m-%d"]) 
    image = forms.ImageField()
    class Meta:
        model = Game

        fields = [
            'name',
            'description',
            'image',
            'release_date',
            'age_rating',
            'genres',
            'developers',
            'platforms',
            'publishers'
        ]
        widgets={
            'description': forms.Textarea(),
            'platforms': forms.Select(),
            'publishers': forms.Select()
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            'name'
        ]
        # widgets={
        #     'name': forms.CharField()
        # }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [
            'name'
        ]
        # widgets={
        #     'name': forms.CharField()
        # }

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = [
            'name'
        ]
        # widgets={
        #     'name': forms.CharField()
        # }

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = [
            'name'
        ]
        # widgets={
        #     'name': forms.CharField()
        # }

class ReviewForm(forms.ModelForm):
    grade_options = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )
    grade = forms.ChoiceField(choices=grade_options)
    #text = forms.TextField()
    #platform = forms.MultipleChoiceField(choices=Game.objects.values_list('id', 'name'))
    class Meta:
        model = Review
        fields=[
            'text',
            'grade'
        ]