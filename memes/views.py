from django.shortcuts import render, redirect, get_object_or_404
from .models import Meme, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MemeForm, CommentForm, ReportMeme
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import searchMeme
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def memes(request):
    """
    This view will display all memes in the database. It will also allow the
    user to search for memes by title or tag.
    """

    memes, search_form = searchMeme(request)

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
        "search_form": search_form,
        }
    return render(request, "memes/memes.html", context)


def meme(request, pk):
    """
    This view will display a single meme.
    """
    memes, search_form = searchMeme(request)

    memeObj = Meme.objects.get(id=pk)
    tags = memeObj.tags.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.userprofile
            comment.meme = memeObj
            comment.save()
            form.save()
        messages.success(request, 'Comment added successfully!')
        return redirect("meme", pk=pk)

    context = {
        "meme": memeObj,
        "tags": tags,
        "memes": memes,
        "search_form": search_form,
        "form": form,
        }
    return render(request, "memes/single-meme.html", context)


def homePage(request):
    """
    This view will display the home page.
    """
    memes, search_form = searchMeme(request)

    context = {
        "memes": memes,
        "search_form": search_form,
        }
    return render(request, "index.html", context)


@login_required(login_url='/accounts/login/')
def uploadMeme(request):
    """
    This view will allow the user to upload a meme.
    """
    memes, search_form = searchMeme(request)

    profile = request.user.userprofile
    form = MemeForm()

    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.uploader = profile
            meme.save()
            form.save()
            messages.success(request, 'Meme uploaded successfully!')
            return redirect("memes")

    context = {
        "form": form,
        "memes": memes,
        "search_form": search_form
        }
    return render(request, "memes/meme_form.html", context)


@login_required(login_url='/accounts/login/')
def updateMeme(request, pk):
    """
    This view will allow the user to update a meme.
    """
    profile = request.user.userprofile
    meme = profile.meme_set.get(id=pk)
    form = MemeForm(instance=meme)

    @property
    def meme_img(self):
        if self.meme_img:
            url = self.meme_img.url
        else:
            url = (
                'images/memes/default.webp'
            )
        return url

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
    """
    This view will allow the user to delete a meme.
    """
    profile = UserProfile.objects.get(user=request.user)
    meme = profile.meme_set.get(id=pk)
    if request.method == 'POST':
        meme.delete()
        messages.warning(request, 'Meme was deleted!')
        return redirect('memes')

    context = {'meme': meme}
    return render(request, "memes/delete_meme.html", context)


def smiley_face(request, pk):
    """
    This view will allow the user to like or add/remove a smiley
    face to the meme.
    """
    if request.user.is_authenticated:
        meme = get_object_or_404(Meme, id=pk)
        if meme.smiley_face.filter(id=request.user.userprofile.id).exists():
            if not meme.sad_face.filter(
                    id=request.user.userprofile.id).exists():

                meme.smiley_face.remove(request.user.userprofile)
                messages.info(request, 'You removed your like!')
        elif not meme.smiley_face.filter(
                id=request.user.userprofile.id).exists():

            if meme.sad_face.filter(id=request.user.userprofile.id).exists():
                meme.sad_face.remove(request.user.userprofile)
                meme.smiley_face.add(request.user.userprofile)
                messages.success(request, 'You turned that frown upside down!')
            else:
                meme.smiley_face.add(request.user.userprofile)
                messages.success(request, 'You liked the meme!')
    else:
        messages.info(request, 'You must be logged in to like a meme!')

    return redirect(request.META.get('HTTP_REFERER'))


def sad_face(request, pk):
    """
    This view will allow the user to dislike or add/remove a
    sad face to the meme.
    """
    if request.user.is_authenticated:
        meme = get_object_or_404(Meme, id=pk)
        if meme.sad_face.filter(id=request.user.userprofile.id).exists():
            if not meme.smiley_face.filter(
                    id=request.user.userprofile.id).exists():

                meme.sad_face.remove(request.user.userprofile)
                messages.info(request, 'You removed your dislike!')
        elif not meme.sad_face.filter(id=request.user.userprofile.id).exists():
            if meme.smiley_face.filter(
                    id=request.user.userprofile.id).exists():

                meme.smiley_face.remove(request.user.userprofile)
                meme.sad_face.add(request.user.userprofile)
                messages.info(request, 'You changed your like to dislike!')
            else:
                meme.sad_face.add(request.user.userprofile)
                messages.info(request, 'You disliked the meme!')
    else:
        messages.info(request, 'You must be logged in to dislike a meme!')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/login/')
def deleteComment(request, pk):
    """
    This view will allow the user to delete a comment.
    """
    profile = UserProfile.objects.get(user=request.user)
    comment = profile.comment_set.get(id=pk)
    if request.method == 'POST':
        comment.delete()
        messages.warning(request, 'Your comment was deleted!')
        return redirect('meme', pk=comment.meme.id)

    context = {'meme': meme}
    return render(request, "memes/delete_comment.html", context)


def custom_404(request, exception):
    """
    This view will display a custom 404 page.
    """
    return render(request, "memes/custom_404.html", status=404)


def custom_500(request):
    """
    This view will display a custom 500 page.
    """
    return render(request, "memes/custom_500.html", status=500)


@login_required(login_url='/accounts/login/')
def reportMeme(request, pk):
    """
    This view will allow the user to report a meme.
    """
    memeObj = Meme.objects.get(id=pk)
    if request.method == 'POST':

        form = ReportMeme(request.POST)
        tm_email = request.user.userprofile.email
        tm_profile = request.user.userprofile.username

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('memes/emails/report_meme_email.html', {
                'name': name,
                'email': email,
                'message': message,
                'meme': memeObj,
                'tm_profile': tm_profile,
                'tm_email': tm_email,
            })

            send_mail('The Report Meme form entry',
                      'The report meme form message',
                      'noreply@test.com', ['intc21@gmail.com'],
                      fail_silently=False, html_message=html)
            messages.success(request, 'Your report was sent!')
            next = request.GET.get('next', 'report-meme')
            return HttpResponseRedirect(next)
    else:
        form = ReportMeme()

    context = {'form': form, 'meme': memeObj}
    return render(request, "memes/report_meme.html", context)
