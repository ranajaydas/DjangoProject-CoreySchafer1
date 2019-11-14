from django.db import models
from django.contrib.auth.models import User  # This is not the best way to do this
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Commented out below because using Amazon S3 for storage
    # def save(self, *args, **kwargs):
    #     """Changes existing save function to resize image before saving."""
    #     super(Profile, self).save(*args, **kwargs)  # Runs the save method of parent class
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
