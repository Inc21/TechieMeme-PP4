from django.shortcuts import render
from django.http import HttpResponse


def memes(request):
    return HttpResponse("Hello, world. You're at the memes index.")


def meme(request, pk):
    return HttpResponse("single meme")
