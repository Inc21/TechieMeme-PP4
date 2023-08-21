from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm


def userProfiles(request):
    profiles = UserProfile.objects.all()
    # memes_uploaded = profiles.meme_set.get()
    context = {'profiles': profiles}
    return render(request, "users/user_profiles.html", context)


def singleUser(request, pk):
    profile = UserProfile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, "users/single_user.html", context)


@login_required(login_url='/accounts/login/')
def updateProfile(request):
    profile = request.user.userprofile
    form = UserForm(instance=profile)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            messages.success(request, 'Profile updated successfully!')
            return redirect('single_user', pk=profile.id)

    context = {'form': form}
    return render(request, "users/user_form.html", context)


@login_required(login_url='/accounts/login/')
def deleteProfile(request, pk):
    profile = UserProfile.objects.get(id=pk)
    if request.method == "POST":
        profile.delete()
        messages.warning(request, 'Profile was deleted!')
        return redirect('/')

    context = {'profile': profile}
    return render(request, "users/delete_user.html", context)


def memesUploaded(request):
    profile = request.user.userprofile
    memes = profile.meme_set.all()
    context = {'memes': memes}
    return render(request, "users/user_profiles.html", context)
