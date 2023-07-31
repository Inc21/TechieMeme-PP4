from django.shortcuts import render


def userProfiles(request):
    return render(request, "users/user_profiles.html")
