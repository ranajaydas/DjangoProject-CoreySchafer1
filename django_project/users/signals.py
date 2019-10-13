"""
Signals run specific functions after certain actions.

User configured functionality:
1. Every time a new User is registered, a Profile is also created.
"""

from django.db.models.signals import post_save  # A signal that gets fired after an object is saved
from django.contrib.auth.models import User     # This is the sender
from django.dispatch import receiver            # This is the receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Runs every time a user is created."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Runs every time a user is saved."""
    instance.profile.save()
