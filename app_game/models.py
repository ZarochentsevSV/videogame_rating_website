from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model



class Developer(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return 'developer'
    def __str__(self):
        return f"Developer: {self.name}"


class Publisher(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return 'publisher'
    def __str__(self):
        return f"Publisher: {self.name}"


class Platform(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return 'platform'
    def __str__(self):
        return f"Platform: {self.name}"

class Genre(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'genre'
    def __str__(self):
        return f"Genre: {self.name}"

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

    def __str__(self):
        return f"Videogame: {self.name}"

class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    grade = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    #platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Review: {self.user}\tGrade: {self.grade}\t{self.game}"
