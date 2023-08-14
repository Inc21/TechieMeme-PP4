from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm


def userProfiles(request):
    profiles = UserProfile.objects.all()
    last_active = User.objects.all().last().last_login
    print(last_active)
    context = {'profiles': profiles, 'last_active': last_active}
    return render(request, "users/user_profiles.html", context)


def singleUser(request, pk):
    profile = UserProfile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, "users/single_user.html", context)


@login_required(login_url='login')
def updateProfile(request):
    profile = request.user.userprofile
    form = UserForm(instance=profile)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('single_user', pk=profile.id)

    context = {'form': form}
    return render(request, "users/user_form.html", context)


@login_required(login_url='login')
def deleteUser(request, pk):
    profile = UserProfile.objects.get(id=pk)
    if request.method == "POST":
        profile.delete()
        return redirect('/')

    context = {'profile': profile}
    return render(request, "users/user_profiles.html", context)
