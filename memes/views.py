from django.shortcuts import render
from .models import Meme


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
