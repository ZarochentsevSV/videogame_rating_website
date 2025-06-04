from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from PIL import Image
import datetime




    

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    day_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        default='avatar.jpg',
        upload_to='profile_avatars',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username}\' Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)