from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def userProfiles(request):
    """
    This view will display all the user profiles and paginate them.
    """

    profiles = UserProfile.objects.all()
    page = request.GET.get('page')
    results = 4
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    context = {
        'profiles': profiles,
        "custom_range": custom_range,
        "paginator": paginator
        }
    return render(request, "users/user_profiles.html", context)


def singleUser(request, pk):
    """
    This view will display a single user profile.
    """
    profile = UserProfile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, "users/single_user.html", context)


@login_required(login_url='/accounts/login/')
def updateProfile(request):
    """
    This view will update the user profile.
    """
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
    """
    This view will delete the user profile.
    """
    profile = UserProfile.objects.get(id=pk)
    if request.method == "POST":
        profile.delete()
        messages.warning(request, 'Profile was deleted!')
        return redirect('/')

    context = {'profile': profile}
    return render(request, "users/delete_user.html", context)


def memesUploaded(request):
    """
    This view will display all the memes uploaded by the user.
    """
    profile = request.user.userprofile
    memes = profile.meme_set.all()
    context = {'memes': memes}
    return render(request, "users/user_profiles.html", context)
