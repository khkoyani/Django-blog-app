from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    picture= models.ImageField(default='default.jpg', upload_to= 'profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        picture = Image.open(self.picture.path)
        if picture.width > 300 and picture.height>300:
            output_size=(300, 300)
            picture.thumbnail(output_size)
            picture.save(self.picture.path)

# Create your models here.
