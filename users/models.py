import uuid
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user_img = ResizedImageField(upload_to='users/', null=True,
                                 force_format='WEBP', quality=85,
                                 blank=True, default='users/default_user.webp')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.username)

    @property
    def user_image_url(self):
        if self.user_img and hasattr(self.user_img, 'url'):
            return self.user_img.url
        else:
            return '/static/images/users/default_user.webp'

    class Meta:
        ordering = ['-created']
