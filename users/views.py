from django.shortcuts import render
from .models import UserProfile


def userProfiles(request):
    profiles = UserProfile.objects.all()
    context = {'profiles': profiles}
    return render(request, "users/user_profiles.html", context)
