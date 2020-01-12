from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . models import Profile

@receiver(post_save , sender=User)
def create_profile(sender , instance, created, **kwargs):
    user = instance
    if created:
        profile=Profile.objects.create(user=instance)
        profile.save()
