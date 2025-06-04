from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Review)