from django.shortcuts import render
from .models import Meme


def memes(request):
    memes = Meme.objects.all()
    context = {"memes": memes}
    return render(request, "memes/memes.html", context)


def meme(request, pk):
    meme = Meme.objects.get(id=pk)
    # print('meme: ', meme)
    return render(request, "memes/single-meme.html", {'meme': meme})


def home_page(request):
    return render(request, "index.html")
