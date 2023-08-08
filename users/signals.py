from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_delete.connect(deleteUser, sender=UserProfile)
