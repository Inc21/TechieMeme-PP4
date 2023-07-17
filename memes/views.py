from django.shortcuts import render


def memes(request):
    return render(request, "memes/memes.html")


def meme(request, pk):
    return render(request, "memes/single-meme.html")
