from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model



class Developer(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Publisher(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Platform(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Genre(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Game(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default="", verbose_name='Image')
    release_date = models.DateField()
    age_rating = models.CharField(max_length=128)
    genres = models.ManyToManyField(Genre)
    developers = models.ManyToManyField(Developer)
    platforms = models.ManyToManyField(Platform)
    publishers = models.ManyToManyField(Publisher)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    grade = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)