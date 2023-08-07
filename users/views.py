from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User


def userProfiles(request):
    profiles = UserProfile.objects.all()
    user = User.objects.get(username=request.user)
    last_login = user.last_login.strftime("%d/%m/%y")
    context = {'profiles': profiles, 'last_login': last_login}
    return render(request, "users/user_profiles.html", context)
