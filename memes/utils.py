from django.db.models import Q
from .models import Meme, Tag
from users.models import UserProfile


def searchMeme(request):
    search_form = ''

    if request.GET.get('search_form'):
        search_form = request.GET.get('search_form')

    tags = Tag.objects.filter(name__icontains=search_form)
    usernames = UserProfile.objects.filter(username__icontains=search_form)

    memes = Meme.objects.distinct().filter(
        Q(title__icontains=search_form) |
        Q(tags__in=tags) |
        Q(uploader__in=usernames)
        )

    return memes, search_form
