from django.shortcuts import render, redirect
from .models import Meme, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MemeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import memeFilter


def memes(request):
    memes = Meme.objects.all()

    page = request.GET.get('page')
    results = 4
    paginator = Paginator(memes, results)

    try:
        memes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        memes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        memes = paginator.page(page)

    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    context = {
        "memes": memes,
        "paginator": paginator,
        "custom_range": custom_range,
        }
    return render(request, "memes/memes.html", context)


def meme(request, pk):
    memeObj = Meme.objects.get(id=pk)
    tags = memeObj.tags.all()

    context = {"meme": memeObj,
               "tags": tags,
               }
    return render(request, "memes/single-meme.html", context)


def homePage(request):
    memes = Meme.objects.all()

    context = {"memes": memes}
    return render(request, "index.html", context)


@login_required(login_url='/accounts/login/')
def uploadMeme(request):
    profile = request.user.userprofile
    form = MemeForm()

    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.uploader = profile
            meme.save()
            messages.success(request, 'Meme uploaded successfully!')
            return redirect("memes")

    context = {'form': form}
    return render(request, "memes/meme_form.html", context)


@login_required(login_url='/accounts/login/')
def updateMeme(request, pk):
    profile = request.user.userprofile
    meme = profile.meme_set.get(id=pk)
    form = MemeForm(instance=meme)

    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES, instance=meme)
        if form.is_valid():
            form.save()

            messages.success(request, 'Meme updated successfully!')
            return redirect('meme', pk=pk)

    context = {'form': form, 'meme': meme}
    return render(request, "memes/meme_form.html", context)


@login_required(login_url='/accounts/login/')
def deleteMeme(request, pk):
    profile = UserProfile.objects.get(user=request.user)
    meme = profile.meme_set.get(id=pk)
    if request.method == 'POST':
        meme.delete()
        messages.warning(request, 'Meme was deleted!')
        return redirect('memes')

    context = {'meme': meme}
    return render(request, "memes/delete_meme.html", context)
