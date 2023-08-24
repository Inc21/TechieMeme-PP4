from django.db import models
import uuid
from users.models import UserProfile


class Meme(models.Model):
    uploader = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    meme_img = models.ImageField(upload_to='memes/',
                                 default='memes/default.webp')
    tags = models.ManyToManyField('Tag', blank=True)
    smiley_face = models.IntegerField(default=0, null=True, blank=True)
    sad_face = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Review(models.Model):
    VOTE_TYPE = (
        ('like', '+1'),
        ('unlike', '-1'),
    )
    # owner = models.ForeignKey(
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=10, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.meme.title.title() + ' - ' + self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
