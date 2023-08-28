from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, ContactMe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from memes.utils import searchMeme
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.urls import reverse


def userProfiles(request):
    """
    This view will display all the user profiles and paginate them.
    """
    memes, search_form = searchMeme(request)

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
        "profiles": profiles,
        "custom_range": custom_range,
        "paginator": paginator,
        "memes": memes,
        "search_form": search_form,
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


@login_required(login_url='/accounts/login/')
def memesUploaded(request):
    """
    This view will display all the memes uploaded by the user.
    """
    profile = request.user.userprofile
    memes = profile.meme_set.all()
    context = {'memes': memes}
    return render(request, "users/user_profiles.html", context)


@login_required(login_url='/accounts/login/')
def contactMe(request):
    """
    This view will display the contact form.
    """
    if request.method == 'POST':
        form = ContactMe(request.POST)
        tm_email = request.user.userprofile.email
        tm_profile = request.user.userprofile.username
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('users/emails/contact_developer.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
                'tm_profile': tm_profile,
                'tm_email': tm_email,
            })

            send_mail('The contact form entry',
                      'The contact form message',
                      'noreply@test.com', ['intc21@gmail.com'],
                      fail_silently=False, html_message=html)
            messages.success(request, 'Message sent successfully!')
            next = request.GET.get('next', reverse('contact-form'))
            return HttpResponseRedirect(next)
    else:
        form = ContactMe()

    context = {'form': form}
    return render(request, "users/contact_form.html", context)
