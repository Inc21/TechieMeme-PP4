from django.shortcuts import render


def memes(request):
    message = "Hello, world. You're at the memes page."
    return render(request, "memes/memes.html", {"message": message})


def meme(request, pk):
    return render(request, "memes/single-meme.html")
