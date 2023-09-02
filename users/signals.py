from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.mail import send_mail
from django.conf import settings


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        UserProfile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

        send_mail(
            subject="Welcome to TechieMeme",
            message=("Welcome to TechieMeme!"
                     "We hope you will have some fun and enjoy your stay."),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created:
        user.username = profile.username
        user.email = profile.email
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)
post_save.connect(updateUser, sender=UserProfile)
post_delete.connect(deleteUser, sender=UserProfile)
