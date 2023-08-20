from django.shortcuts import render, redirect
from .models import Meme
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MemeForm


def memes(request):
    memes = Meme.objects.all()
    context = {"memes": memes}
    return render(request, "memes/memes.html", context)


def meme(request, pk):
    memeObj = Meme.objects.get(id=pk)
    tags = memeObj.tags.all()
    context = {"meme": memeObj, "tags": tags}
    return render(request, "memes/single-meme.html", context)


def home_page(request):
    memes = Meme.objects.all()
    context = {"memes": memes}
    return render(request, "index.html", context)


@login_required(login_url='/accounts/login/')
def uploadMeme(request):
    form = MemeForm()

    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Meme uploaded successfully!')
            return redirect("memes")

    context = {'form': form}
    return render(request, "memes/meme_form.html", context)
