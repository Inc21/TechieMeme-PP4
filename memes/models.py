from django.db import models
import uuid
from users.models import UserProfile
from django_resized import ResizedImageField


class Meme(models.Model):
    uploader = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    meme_img = ResizedImageField(upload_to='memes/',
                                 force_format='WEBP', quality=85,
                                 blank=True, default='memes/default.webp')
    tags = models.ManyToManyField('Tag', blank=True)
    smiley_face = models.ManyToManyField(
        UserProfile, related_name='smiley_face', blank=True)
    sad_face = models.ManyToManyField(
        UserProfile, related_name='sad_face', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

# returns the total number of likes or smiley faces
    def total_smiley_face(self):
        return self.smiley_face.count()

# returns the total number of dislikes or sad faces
    def total_sad_face(self):
        return self.sad_face.count()

    def __str__(self):
        return self.title

# Replaces default image incase the user deletes the image
    @property
    def meme_image_url(self):
        if self.meme_img and hasattr(self.meme_img, 'url'):
            return self.meme_img.url
        else:
            return '/static/images/memes/default.webp'

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    """
    This class is used to create a model for the meme comments.
    """
    meme = models.ForeignKey(
        Meme, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user.username + ' - ' + self.comment

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    """
    This class is used to create a model for the tags.
    """
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ContactForm(models.Model):
    """
    This class is used to create a model for the contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name + ' - ' + self.email

    class Meta:
        ordering = ['-created']
